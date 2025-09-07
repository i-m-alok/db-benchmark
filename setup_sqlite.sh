#!/bin/bash
# Bash script to install sqlite3 and set up a database

# Install sqlite3 (macOS)
echo "Installing sqlite3..."
brew install sqlite3

# Create a new SQLite database and a sample table
echo "Setting up benchmark.db..."
sqlite3 benchmark.db <<EOF

# Create tables for a blog site
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    dob DATE
);

CREATE TABLE IF NOT EXISTS blog (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    body TEXT,
    excerpt TEXT,
    updated_at TIMESTAMP,
    published_at TIMESTAMP,
    is_deleted BOOLEAN DEFAULT 0,
    slug TEXT,
    FOREIGN KEY(user_id) REFERENCES user(id)
);

CREATE TABLE IF NOT EXISTS tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS blog_tags (
    blog_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    PRIMARY KEY (blog_id, tag_id),
    FOREIGN KEY(blog_id) REFERENCES blog(id),
    FOREIGN KEY(tag_id) REFERENCES tags(id)
);
EOF

echo "SQLite database 'benchmark.db' created and initialized."
