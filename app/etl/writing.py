
import sqlalchemy
from app.etl.Transforming_data import transforming_data
host = 'localhost'
port = '5433'
database = 'itversity_energy_db'
user = 'itversity_energy_user'
password = 'energy_password'

energy_connection = sqlalchemy.create_engine(
    "postgresql://itversity_energy_user:energy_password@localhost:5433/itversity_energy_db")

data = transforming_data(sample_path)
data.to_sql('energy_database', energy_connection)