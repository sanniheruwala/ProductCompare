# ProductCompare
Product compare using fastapi, streamlit and docker. It provides support for batch load of product files and also demonstration of streamlit UI as a data app.

# Steps to run App
#### Step 1 : Git clone
```
git clone https://github.com/sanniheruwala/ProductCompare.git
```
#### Step 2 : Go to root directory
```
cd ProductCompare
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
### Bingo !!! Your application is running.

## Go to web app
> localhost:8051

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
