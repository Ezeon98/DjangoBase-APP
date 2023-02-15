# DjangoBase-APP
## Steps to execute

cd DjangoBase

docker-compose build

docker-compose up

Exercise 1:
Go to http://localhost:8000/app/valerdat/products/

Exercise 2:
Execute DjangoBase/app/utils/word_finder.py

Excercise 3:
Execute DjangoBase/app/utils/add_products.py
Go to http://localhost:8000/app/valerdat/searchcoords/?product=nbxljsniyfsimjxt --> Retrieve a HTTP Error
Go to http://127.0.0.1:8000/app/valerdat/searchcoords/?product=lslikrwsjalbcqeq --> Retrieve a product in JSONResponse

To Do:
-Unit Tests, especially in SearchCoordView
-Execute add_products.py in dockerization and validate if products exists.
