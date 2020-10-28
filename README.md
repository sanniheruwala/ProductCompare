# ProductCompare
Product compare using fastapi, streamlit and docker. It provides support for batch load of product files and also demonstration of streamlit UI as a data app.

This app uses docker. Make sure it is available in you local machine.

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
Application will be available on `localhost` in your browser.

# Bingo !!! Your application is running.

## Go to web app
> http://localhost:8501/

## To access backend API/ FastAPI - Swagger UI
> http://localhost:8000/docs
> http://localhost:8000/redoc

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
