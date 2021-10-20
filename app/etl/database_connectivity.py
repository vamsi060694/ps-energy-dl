import psycopg2
from app.etl.Transforming_data import transforming_data

host = 'localhost'
port = '5433'
database = 'itversity_energy_db'
user = 'itversity_energy_user'
password = 'energy_password'


def get_pg_connection(host, port, database, user, password):
    connection = None
    try:
        connection = psycopg2.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
    except Exception as e:
        raise (e)

    return connection

energy_connection = get_pg_connection(host, port, database, user, password)

cursor = energy_connection.cursor()
query = ("""
    INSERT INTO users
        (well_name, month, Comodity, Value, energy, units)
    VALUES
        (%s, %s, %s, %s, %s, %s)
""")

user = transforming_data(sample_path)
cursor.execute(query, user)
energy_connection.commit()

cursor.close()
energy_connection.close()
