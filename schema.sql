CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT,
    admin INTEGER
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    name TEXT,
    author TEXT,
    description TEXT,
    genre TEXT, 
    stars INTEGER,
    visible INTEGER
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users, 
    username TEXT, 
    book_id INTEGER REFERENCES books, 
    stars INTEGER, 
    review TEXT, 
    time TIMESTAMP, 
    visible INTEGER);
