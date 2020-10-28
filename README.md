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
# Performace - Flask vs FastAPI

### Flask
```
Concurrency Level:      500
Time taken for tests:   27.827 seconds
Complete requests:      5000
Failed requests:        0
Total transferred:      830000 bytes
HTML transferred:       105000 bytes
Requests per second:    179.68 [#/sec] (mean)
Time per request:       2782.653 [ms] (mean)
Time per request:       5.565 [ms] (mean, across all concurrent requests)
Transfer rate:          29.13 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0   87 293.2      0    3047
Processing:    14 1140 4131.5    136   26794
Waiting:        1 1140 4131.5    135   26794
Total:         14 1227 4359.9    136   27819

Percentage of the requests served within a certain time (ms)
  50%    136
  66%    148
  75%    179
  80%    198
  90%    295
  95%   7839
  98%  14518
  99%  27765
 100%  27819 (longest request)
 ```

### FastAPI
```
Concurrency Level:      500
Time taken for tests:   0.577 seconds
Complete requests:      5000
Failed requests:        0
Total transferred:      720000 bytes
HTML transferred:       95000 bytes
Requests per second:    8665.48 [#/sec] (mean)
Time per request:       57.700 [ms] (mean)
Time per request:       0.115 [ms] (mean, across all concurrent requests)
Transfer rate:          1218.58 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    6   4.5      6      30
Processing:     6   49  21.7     45     126
Waiting:        1   42  19.0     39     124
Total:         12   56  21.8     53     127

Percentage of the requests served within a certain time (ms)
  50%     53
  66%     64
  75%     69
  80%     73
  90%     81
  95%     98
  98%    112
  99%    116
 100%    127 (longest request)
```

### Total results
```
Flask: Time taken for tests: 27.827 seconds

FastAPI - Uvicorn: Time taken for tests: 1.562 seconds

FastAPI - Uvicorn Workers: Time taken for tests: 0.577 seconds
```



