from flask import Flask, send_file
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

@app.route('/category/<cat_slug>')
def category_route(cat_slug):

    cat_instance = db('categories')

    rows = cat_instance.select(f"WHERE slug='{cat_slug}'")

    if len(rows):
        row = rows[0]
        
        temp_cat = {
             "id": row[0],
             "name": row[1],
             "slug": row[2],
             "desc": row[3],
             "img": row[4]
        }

        return temp_cat
    else:
        return {}

@app.route('/products')
def products_route():
     prod_instance = db('products')

     temp_products = []

     rows = prod_instance.select()

     for row in rows:
          temp_prod ={
               "id": row[0],
               "prod_name": row[1],
               "prod_img": row[2],
               "prod_desc": row[3],
               "prod_slug": row[4],
               "prod_price": row[5]

          }
          
          temp_products.append(temp_prod)

     products_dict = {
          "products": temp_products
     }

     return temp_products

@app.route('/product/<prod_slug>')
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

@app.route('/category/<cat_slug>')
def product_route(prod_slug):

    prod_instance = db('categories')

    rows = prod_instance.select(f"WHERE prod-slug='{prod_slug}'")

    if len(rows):
        row = rows[0]
        
        temp_prod = {
             "id": row[0],
             "prod_name": row[1],
             "prod_img": row[2],
             "prod_desc": row[3],
             "prod_slug": row[4]
        }

        return temp_prod
    else:
        return {}

@app.route('/images/<img_name>')
def get_image(img_name):
    print(img_name)
    filename = f'images/(img_name)'

    return send_file(filename, minetype='image/jpg')
