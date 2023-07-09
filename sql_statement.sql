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
