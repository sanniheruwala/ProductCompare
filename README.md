# ProductCompare
Product compare using fastapi, streamlit and docker. It provides support for batch load of product files and also demonstration of streamlit UI as a data app.

This app uses docker. Make sure it is available in you local machine.

![Alt text](https://github.com/sanniheruwala/ProductCompare/blob/master/images/Demo.gif)


# Installation
#### Step 1 : Git clone
```
git clone https://github.com/sanniheruwala/ProductCompare.git
```
#### Step 2 : Go to root directory
```
cd ProductCompare/
```
#### Step 3 : Checkout master branch
```
git checkout master
```
#### Step 4 : Build docker container
```
docker-compose build
```
#### Step 5 : Run all apps
```
docker-compose up -d
```

![alt text](https://github.com/sanniheruwala/ProductCompare/blob/master/images/container.png)
![alt text](https://github.com/sanniheruwala/ProductCompare/blob/master/images/image.png)

Application will be available on `localhost` in your browser.

# Bingo !!! Your application is running.

## Go to web app
> http://localhost:8501/

![alt text](https://github.com/sanniheruwala/ProductCompare/blob/master/images/UI.png)

## To access backend API/ FastAPI - Swagger UI
> http://localhost:8000/docs

![alt text](https://github.com/sanniheruwala/ProductCompare/blob/master/images/Swagger.png)


## Project structure
```
ProductCompare
├── Db                            - Database setup.      
│   └── init.sql                  - Table schemas.     
├── ProductCompareService         - FastAPI webservice 
│   ├── Dockerfile                - Commands to run API
│   ├── ProductCompareFast.py     - Main app
│   └── requirements.txt          - Dependencies 
├── ProductCompareWeb             - Streamlit web UI
│   ├── Dockerfile                - Commands to run UI
│   ├── ProductCompareFast.py     - Main app
│   └── requirements.txt          - Dependencies               
└── docker-compose.yml            - Container setup        
```

## Data requirement - Batch load
For batch load data has to be inline with following schema.
```
root
 |-- product_name: string (nullable = true)
 |-- price: string (nullable = true)
 |-- rating: string (nullable = true)
 |-- category: string (nullable = true)
 |-- product_description: string (nullable = true)
 |-- customer_reviews: string (nullable = true)
 |-- url: string (nullable = true)
 |-- website: string (nullable = true)

+--------------------+------+------------------+--------+--------------------+--------------------+--------------------+-------+
|        product_name| price|            rating|category| product_description|    customer_reviews|                 url|website|
+--------------------+------+------------------+--------+--------------------+--------------------+--------------------+-------+
|walmart's Hornby ...|  4.42|               4.6| Hobbies|Product Descripti...|good product Wort...|http://www.walmar...|walmart|
|walmart's FunkyBu...| 17.99|               4.2| Hobbies|Size Name:Large F...|good product Four...|http://www.walmar...|walmart|
|walmart's CLASSIC...| 10.99|               3.6| Hobbies|BIG CLASSIC TOY T...|good product **Hi...|http://www.walmar...|walmart|
|walmart's Hornby ...| 33.19|               4.4| Hobbies|Product Descripti...|good product Birt...|http://www.walmar...|walmart|
|walmart's 20pcs M...|  7.99|               4.7| Hobbies|These delicate mo...|good product Five...|http://www.walmar...|walmart|
+--------------------+------+------------------+--------+--------------------+--------------------+--------------------+-------+
```


