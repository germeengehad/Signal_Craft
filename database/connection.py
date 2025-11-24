from sqlalchemy import create_engine
import psycopg2
import os

def get_engine():
    DB_USER = "postgres"
    DB_PASSWORD = "1999"
    DB_HOST = "localhost"
    DB_PORT = "5432"
    DB_NAME = "signalcraft_db"

    url = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(url)
    return engine
