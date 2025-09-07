# Database Benchmarking: SQLite3 Setup

This project sets up a SQLite3 database for benchmarking blog site performance.

## Prerequisites
- macOS (Homebrew recommended)
- SQLite3

## Setup Instructions

1. **Install SQLite3 and create tables:**
   Run the setup script to install SQLite3 and create the required tables:
   
   ```bash
   bash setup_sqlite.sh
   ```

2. **Check tables:**
   To list all tables in the database:
   ```bash
   sqlite3 benchmark.db ".tables"
   ```
   To view the schema of a table:
   ```bash
   sqlite3 benchmark.db ".schema table_name"
   ```
3. **Run SQL queries:**
    Open the database
    ```bash
    sqlite3 benchmark.db
    ```
    Then run SQL queries,
    ```bash
    SELECT * FROM user LIMIT 10;
    ```
## Tables Created
- `user`: Stores user information
- `blog`: Stores blog posts
- `tags`: Stores tags
- `blog_tags`: Many-to-many relationship between blogs and tags

## Script Reference
The main setup script is [`setup_sqlite.sh`](setup_sqlite.sh).

---
