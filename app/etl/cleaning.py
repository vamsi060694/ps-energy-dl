path = 'C:\workspace\ps-energy-dl\data_folder\hibernia'
import numpy as np
from app.etl.extraction import extraction


new_tables = extraction(path)


def cleaning(new_tables):
    all_columns = new_tables.columns
    for columns in ['Well Name', 'Year', 'Month', 'Oil (m³)', 'Gas (10³m³)', 'Water (m³)']:
        new_tables[columns] = new_tables[columns].replace('', np.NAN)
        for columns in ['Well Name', 'Year', 'Month']:
            new_tables[columns] = new_tables[columns].fillna(method='ffill')
    return new_tables