# Dummy data generator for SQLite blog benchmarking
import sqlite3
import random
from faker import Faker
import os

DB_PATH = 'benchmark.db'
NUM_USERS = 10000
NUM_BLOGS = 10000
NUM_TAGS = 1000
NUM_BLOG_TAGS = 20000
LARGE_BODY_COUNT = 5000
LARGE_BODY_SIZE = 100 * 1024  # 100KB

fake = Faker()
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Insert users
def insert_users():
    users = [
        (fake.first_name(), fake.last_name(), fake.date_of_birth(minimum_age=18, maximum_age=80).isoformat())
        for _ in range(NUM_USERS)
    ]
    cursor.executemany('INSERT INTO user (first_name, last_name, dob) VALUES (?, ?, ?)', users)
    conn.commit()

# Insert tags
def insert_tags():
    # existing_tags = set()
    # while len(existing_tags) < NUM_TAGS:
    #     tag = fake.word()
    #     existing_tags.add(tag)
    # tags = [(tag,) for tag in existing_tags]
    tags = [(f"tag_{i}",) for i in range(1, NUM_TAGS + 1)]
    cursor.executemany('INSERT INTO tags (name) VALUES (?)', tags)
    conn.commit()

# Insert blogs
def insert_blogs():
    blogs = []
    for i in range(NUM_BLOGS):
        user_id = random.randint(1, NUM_USERS)
        title = fake.sentence(nb_words=6)
        excerpt = fake.text(max_nb_chars=200)
        updated_at = fake.date_time_this_year().isoformat()
        published_at = fake.date_time_this_year().isoformat()
        is_deleted = random.choice([0, 1]) if random.random() < 0.05 else 0
        slug = fake.slug()
        if i < LARGE_BODY_COUNT:
            body = fake.text(max_nb_chars=LARGE_BODY_SIZE)
        else:
            body = fake.text(max_nb_chars=5000)
        blogs.append((user_id, title, body, excerpt, updated_at, published_at, is_deleted, slug))
    cursor.executemany('''INSERT INTO blog (user_id, title, body, excerpt, updated_at, published_at, is_deleted, slug) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', blogs)
    conn.commit()

# Insert blog_tags
def insert_blog_tags():
    blog_tags = set()
    while len(blog_tags) < NUM_BLOG_TAGS:
        blog_id = random.randint(1, NUM_BLOGS)
        tag_id = random.randint(1, NUM_TAGS)
        blog_tags.add((blog_id, tag_id))
    cursor.executemany('INSERT INTO blog_tags (blog_id, tag_id) VALUES (?, ?)', list(blog_tags))
    conn.commit()

if __name__ == "__main__":
    print("Inserting users...")
    insert_users()
    print("Inserting tags...")
    insert_tags()
    print("Inserting blogs...")
    insert_blogs()
    print("Inserting blog_tags...")
    insert_blog_tags()
    print("Dummy data generation complete.")
    conn.close()
