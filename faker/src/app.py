import json
import os

import numpy as np
import pandas as pd
import psycopg2
from dotenv import load_dotenv
from sqlalchemy import create_engine

from custom_provider import MarketProvider
from faker import Faker

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

fake = Faker()
fake.add_provider(MarketProvider)


def get_postgres_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )


def produce_fake_record():
    complete_name = fake.name()
    complete_name_split = complete_name.split(" ")
    first_name = " ".join(complete_name_split[::-1])
    last_name = complete_name_split[-1]
    email = fake.email()
    item = fake.product()
    item_quantity = np.random.randint(low=0, high=10)

    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "item": item,
        "item_quantity": item_quantity,
    }


if "__name__" == "__main__":
    import time
    counter = 0
    while counter < 1000:
        engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        record = produce_fake_record()
        df = pd.DataFrame.from_dict([record])
        df.to_sql("market", engine, if_exists="append", index=False)
        #time.sleep(0.05)