#!/usr/bin/env python
# coding: utf-8
# streamlit run ProductCompareUI.py
# docker-compose build
# docker-compose up -d

import pandas as pd
import requests
import streamlit as st
from requests_toolbelt.multipart.encoder import MultipartEncoder

# """ Web App header """
st.title('Product compare App')

# """ Set width of the page. """
max_width_str = f"max-width: 900px;"
st.markdown(f"""<style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """, unsafe_allow_html=True)

# """ File upload type allowed. """
FILE_TYPES = ["csv"]

# """ Header colour mark down. """
st.markdown('<style>h2{color: red;}</style>', unsafe_allow_html=True)

# """ File uploader function, which calls REST Api to upload file into database. """
st.header("Batch load new products")
uploaded_file = st.file_uploader("Choose a file", type=FILE_TYPES)

if uploaded_file:
    file = MultipartEncoder(fields={'file': (uploaded_file.name, uploaded_file, 'text/csv')})
    res = requests.post('http://fastapi:8000/batchLoad/', data=file, headers={'Content-Type': file.content_type})
    st.markdown(res.content.decode("utf-8"))

# """ Product  search option to compare. """
st.header("Search product to compare")
st.subheader("Product name")
product_name = st.text_input("", "Moshi Rox Tin Game")
st.subheader("Category")
category = st.text_input(" ", "Play")
submit = st.button("Search")

# """ If submit clicked then call REST Api and show formatted data in UI. """
if submit:
    resp = requests.get('http://fastapi:8000/match/{productName}/' + category + '?product_name=' + product_name).json()
    df = pd.DataFrame.from_dict(resp)
    if len(df) > 0:
        pro_name = df['pro_name'].tolist()
        cat_name = df['cat_name'].tolist()
        description = df['description'].tolist()
        price = df['price'].tolist()
        rating = df['rating'].tolist()
        url = df['url'].tolist()
        web_name = df['web_name'].tolist()
        st.subheader("Search result")
        for i in range(len(pro_name)):
            st.code("Product : " + pro_name[i] + "\n" + "Category : " + cat_name[i] + "\n" + "Description : " +
                    description[i] + "\n" + "Price : " + price[i] + "\n" + "Rating : " + rating[i] + "\n" + "URL : " +
                    url[i] + "\n" + "Seller : " + web_name[i])
    else:
        st.subheader("No result found")
