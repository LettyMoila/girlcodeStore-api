from flask import Flask
from flask_cors import CORS

import config
from db import db

app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
    return "Girlcode Store API"

@app.route('/categories')
def categories_route():
    top_categories = []

    cat_instance = db('categories')

    rows = cat_instance.select()

    for row in rows:
        temp_cat = {
            "id": row[0],
            "name": row[1],
            "slug": row[2],
            "desc": row[3],
            "img": row[4]
        }
    
    top_categories.append(temp_cat)

    categories_dict = {
        "categories": top_categories
    }

    return  categories_dict