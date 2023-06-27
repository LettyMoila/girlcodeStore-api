from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
    return "Girlcode Store API"

@app.route('/categories')
def categories_route():
    top_categories = [
        {
            "name": "furniture",
            "path": "/category/furniture"
        },
          {
            "name": "Hand bag",
            "path": "/category/hand-bag"
        },
        {
           "name": "Books",
           "path": "/category/books",
        },
        {
            "name": "Tech",
            "path": "/category/tech"
        },
        {
            "name": "Sneakers",
            "path": "/category/sneakers"
        },
        {
            "name": "Travel",
            "path": "/category/travel"
        }
    ]

    categories_dict = {
        "categories": top_categories
    }

    return  categories_dict