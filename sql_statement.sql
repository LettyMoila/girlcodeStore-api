--Create Categories Table
CREATE TABLE categories(
    id SERIAL PRIMARY KEY,
    cat_name TEXT NOT NULL UNIQUE,
    slug TEXT NOT NULL UNIQUE,
    cat_desc TEXT 
);

--insert Categories
INSERT INTO categories (cat_name, slug)
VALUES ('Furniture', 'furniture'),
	('Hand Bag', 'hand-bag'),
	('Books', 'books'),
	('Tech', 'tech'),
	('Sneaker', 'sneaker'),
	('Travel', 'travel');
	
	--Add cat_img column on categories
	ALTER TABLE categories
	ADD cat_img TEXT;
	
	UPDATE categories
	SET cat_img='cat_img.jpg';
	
	--create products table
	CREATE TABLE products (
	id SERIAL PRIMARY KEY,
	prod_name TEXT NOT NULL UNIQUE,
	prod_img TEXT NOT NULL UNIQUE,
	prod_desc TEXT,
	prod_slug TEXT NOT NULL UNIQUE,
	prod_price DOUBLE PRECISION NOT NULL
);

--Insert mini ipod product
INSERT INTO products (prod_name, prod_img, prod_desc, prod_slug, prod_price)
VALUES ('Insta Mini 9', 'insta-mini-9.png', 'Selfie mode and selfie mirrow, Macro mode', 'insta-mini-9', 99.85);

--create table for product from category
CREATE TABLE categories_products (
	id SERIAL PRIMARY KEY,
	cat_id INT NOT NULL,
	prod_id INT NOT NULL,
	UNIQUE (cat_id, prod_id),
	FOREIGN KEY(cat_id) REFERENCES categories(id), 
	FOREIGN KEY(prod_id) REFERENCES products(id)
);

INSERT INTO categories_products (cat_id, prod_id)
VALUES (4, 1);

SELECT * FROM categories_products
FULL OUTER JOIN categories on categories_products.cat_id=categories.id
FULL OUTER JOIN products on categories_products.prod_id=products.id
WHERE categories.slug='tech'