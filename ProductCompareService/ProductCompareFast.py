#!/usr/bin/env python
# coding: utf-8
# export LC_ALL=en_US.utf-8
# export LANG=en_US.utf-8
# uvicorn ProductCompareFast:app --reload

import pandas as pd
from fastapi import FastAPI, File, UploadFile, Response
from sqlalchemy import create_engine

app = FastAPI()

app.__doc__ = "Instantiate FastAPI object. This is entry point for api."

"""Allowed extension for batch load is just csv. It can be further improved by adding more."""
ALLOWED_EXTENSIONS = {'csv'}
"""Api will interact with mysql database. Here we are using pymysql as connector."""
db_connection_str = 'mysql+pymysql://root:admin@2020@mysql/ProductCompare'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


allowed_file.__doc__ = "Filter out only supported file format."


@app.get("/match/{productName}/{category}")
async def match(product_name, category):
    sql = """select pro_name,cat_name,description,price,rating,url,web_name from ProductCompare.product_description a 
            join ProductCompare.category b on a.cat_id = b.cat_id
            join ProductCompare.products c on a.pro_id = c.pro_id
            join ProductCompare.review d on a.rew_id = d.rew_id 
            where lower(pro_name) like lower('%""" + product_name + """%') and 
            lower(cat_name) like lower('%""" + category + """%') order by rating DESC"""
    db_connection = create_engine(db_connection_str)
    output = pd.read_sql(sql, db_connection)
    return output


match.__doc__ = """Provide search result based on product name and category. 
It calls database and return pandas dataframe, which is basically json. Since it is async method, 
it is highly capable of handling multiple request at a time."""


def read(table):
    db_connection = create_engine(db_connection_str)
    df = pd.read_sql_table(table, con=db_connection)
    db_connection.dispose()
    return df


read.__doc__ = "Helper method to read table from mysql database. It uses sqlAlchemy as connector."


def write(data, table):
    db_connection = create_engine(db_connection_str)
    data.to_sql(name=table, con=db_connection, if_exists='append', index=False)
    db_connection.dispose()


write.__doc__ = "Helper method to write pandas dataframe into mysql database. It uses sqlAlchemy as connector."


@app.post("/push/{object}")
async def push(object):
    return Response("Yet to implement.", status_code=400)


push.__doc__ = "Provide endpoint to insert single product into database. It is yet to implement."


@app.get("/pull/{object}")
async def pull(object):
    return Response("Yet to implement", status_code=400)


push.__doc__ = "Provide endpoint to pull single product into database. It is yet to implement."


@app.post("/batchLoad/")
async def batchLoad(file: UploadFile = File(...)):
    if file and allowed_file(file.filename):
        read_products = await readFile(file)
        category = await insertData(read_products, "category", ["cat_name"])
        products = await insertData(read_products, "products", ["pro_name", "web_name"])
        review = await insertData(read_products, "review", ["review", "rating"])

        description = read_products.merge(category, how='inner', on=['cat_name']). \
            merge(products, how='inner', on=['pro_name', 'web_name']). \
            merge(review, how='inner', on=['review', 'rating'])[
            ['pro_id', 'cat_id', 'rew_id', 'price', 'description', 'url']]

        await insertData(description, "product_description",
                         ['pro_id', 'cat_id', 'rew_id', 'price', 'description', 'url'])
        return Response("Products loaded successfully.")
    else:
        return Response("Sorry. We are working hard on adding new file types, but as of now please use csv.",
                        status_code=400)


batchLoad.__doc__ = """Provide endpoint to batch import multiple products into database. 
It uses pandas for data selection and normalization. It insert into category, product, review to get numerical value 
corresponds to their categorical value and uses them to create product_description table. As of now only csv support 
provide for batch load. In future it can be expandable to other extensions as well."""


async def readFile(file):
    data = pd.DataFrame(list(map(lambda s: s.decode("utf-8").replace("\n", "").split(","), file.file.readlines())))
    headers = data.iloc[0]
    read_products = pd.DataFrame(data.values[1:], columns=headers)[['product_name', "price", "rating",
                                                                    "category", "product_description",
                                                                    "customer_reviews", "url", "website"]]. \
        rename(columns={"category": "cat_name", "product_name": "pro_name", "customer_reviews": "review",
                        "website": "web_name", "product_description": "description"})
    return read_products


readFile.__doc__ = """This is helper function of batchload. This function read input data csv/file in pandas and select 
                    only useful columns. It also rename it to make it generic for future join conditions."""


async def insertData(data, table, cols):
    new_cat = data[cols].drop_duplicates(). \
        merge(read(table)[cols].drop_duplicates(), on=cols, how='left', indicator=True). \
        query("_merge=='left_only'")
    del new_cat["_merge"]
    write(new_cat, table)
    df = read(table)
    return df


insertData.__doc__ = """This is helper function of batchload. This function check for new metadata value from 
incoming data and update relevant table into database. """
