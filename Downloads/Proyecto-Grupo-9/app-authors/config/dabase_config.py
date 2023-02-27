import psycopg2
import os


def connection():
    return psycopg2.connect(
        database=os.getenv("DATABASE_NAME"),
        host=os.getenv("DATABASE_HOST"),
        user=os.getenv("DATABASE_USERNAME"),
        password=os.getenv("DATABASE_PASSWORD"),
        port=os.getenv("DATABASE_PORT"))
