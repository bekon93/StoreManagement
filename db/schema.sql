DROP TABLE IF EXISTS items;
CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    price FLOAT(10,2) NOT NULL
);


DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 name VARCHAR(255) NOT NULL,
 position VARCHAR(255) NOT NULL,
 wage INTEGER NOT NULL
);


DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
 itemlist VARCHAR(255) NOT NULL,
 total FLOAT(10,2) NOT NULL
);