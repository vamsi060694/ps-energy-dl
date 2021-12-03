import os
import sqlalchemy as sqlalchemy
from dotenv import load_dotenv
import logging

load_dotenv()


def db_connection():
    try:
        host = os.getenv('DB_HOST')
        port = os.getenv('DB_PORT')
        database = os.getenv('DB_NAME')
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        en_connection = sqlalchemy.create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")
        return en_connection
    except Exception as e:
        logging.error(e)


db_connection()
