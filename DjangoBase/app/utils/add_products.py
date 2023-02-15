import json
import requests
import os

dir_path = os.path.dirname(os.path.abspath(__file__))

json_file = os.path.join(dir_path, "products.json")

with open(json_file) as f:
    products = json.load(f)

for i in products['products']:
    requests.post('http://localhost:8000/app/valerdat/products/', data=i)