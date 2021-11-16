import sqlalchemy as sqlalchemy
import os
import datetime as dt
import pandas as pd
from dotenv import load_dotenv
import json

load_dotenv()
host = os.getenv('HOST')
port = os.getenv('PORT')
database = os.getenv('DATABASE')
user = os.getenv('USER')
password = os.getenv('PASSWORD')
filters = os.getenv('REFERENCE').split(',')


def db_connection(host, port, database, user, password):
    en_connection = sqlalchemy.create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")
    return en_connection


energy_connection = db_connection(host, port, database, user, password)
meta = sqlalchemy.MetaData()

for filter in filters:
    field = json.loads(os.getenv('FIELDS'))[filter]
    field_table = sqlalchemy.Table('field_table', meta,
                                   sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
                                   sqlalchemy.Column('field_name', sqlalchemy.String(15)),
                                   sqlalchemy.Column('date_created', sqlalchemy.DateTime(), default=dt.date.today())
                                   )
    meta.create_all(energy_connection)
    field = json.loads(os.getenv('FIELDS'))[filter]
    print(field)
    if field not in field_table.field_name.values:
        query = f"INSERT INTO field_table(field_name) VALUES ('{field}')"
        energy_connection.execute(query)

well_data = pd.read_csv(r'csv_file.csv', header=0, sep=',')
well_list = sorted(list(set(well_data['Well Name'])))
print(well_list)
print(len(well_list))

well_table = sqlalchemy.Table('well_table', meta,
                              sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
                              sqlalchemy.Column('field_id', sqlalchemy.Integer),
                              sqlalchemy.Column('well_name', sqlalchemy.String(20)),
                              sqlalchemy.Column('date_created', sqlalchemy.DateTime(), default=dt.date.today()))
meta.create_all(energy_connection)
for i in well_list:
    if i not in well_table.well_name.values:
        query = f"INSERT INTO well_table(well_name) VALUES ('{i}')"
        energy_connection.execute(query)
