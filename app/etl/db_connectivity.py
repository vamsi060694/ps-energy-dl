import sqlalchemy
import pandas as pd
import logging

energy_connection = sqlalchemy.create_engine(f"postgresql://itv000457_sms_user:ao980r18weik6fq5xe8elazcm29ejsd0@m01.itversity.com:5433/itv000457_sms_db")


meta = sqlalchemy.MetaData()
energy_table = sqlalchemy.Table(
    'energy_table', meta,
    # sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('Well_Name', sqlalchemy.String),
    sqlalchemy.Column('Month', sqlalchemy.DATE),
    sqlalchemy.Column('Comodity', sqlalchemy.String),
    sqlalchemy.Column('Value', sqlalchemy.FLOAT),
    sqlalchemy.Column('energy_product_id', sqlalchemy.INT),
    sqlalchemy.Column('energy_unit_id', sqlalchemy.INT)
)


units_data = pd.read_csv(r'units.csv', header=0, sep=',')
product_data = pd.read_csv(r'energy.csv', header=0, sep=',')


def transforming_data(transform_path, product_data, units_data):
    try:
        sample_data = pd.read_csv(transform_path, header=0, sep=',')
        sample_data.columns = ['ID', 'Well_Name', 'Month', 'crude_oil(m3)', 'natural_gas(km3)', 'other(m3)']
        transpose_data = pd.melt(sample_data, id_vars=['Well_Name', 'Month'],
                                 value_vars=['crude_oil(m3)', 'natural_gas(km3)', 'other(m3)'], var_name='Comodity',
                                 value_name='Value')
        transpose_data[['energy', 'units']] = transpose_data['Comodity'].str.split('(', expand=True)
        transpose_data['units'] = transpose_data['units'].str.replace('[)]', '', regex=True)
        transpose_data['energy_product_id'] = transpose_data.energy.str.lower().map(product_data.set_index('energy_product')['ID'])
        transpose_data['energy_unit_id'] = transpose_data.units.str.lower().map(units_data.set_index('uom')['unit_of_measure_id'])
        transpose_data = transpose_data.drop('energy', axis=1)
        transpose_data = transpose_data.drop('units', axis=1)
        return print(transpose_data)
    except Exception as e:
        logging.error(e)


transforming_data(r'csv_file.csv', product_data, units_data)


conn = energy_connection.connect()
meta.create_all(energy_connection)
db_data = energy_table.insert().values(pd.DataFrame(transforming_data(r'csv_file.csv', product_data, units_data)))

result = conn.execute(db_data)
print(result.inserted_primary_key)

query = 'SELECT * FROM energy_table'
df = pd.read_sql(query, energy_connection)
print(df)
