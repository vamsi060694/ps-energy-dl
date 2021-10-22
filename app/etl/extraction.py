import os
import camelot
import numpy as np
import pandas as pd

from app.utils.logging_init import init_logger
logger = init_logger()
path = 'C:\workspace\ps-energy-dl\data_folder\hibernia'


def extraction(path):
    global all_tables
    for path, dirs, files in os.walk(path):
        for file in files:
            # print(file)
            filename = os.path.join(path, file)
            tables = camelot.read_pdf(filename, pages='all', flavor='stream', edge_tol=1000)
            num = tables.n
            logger.info(num)
            all_tables = pd.DataFrame()
            for i in range(num):
                temp_df = tables[i].df
                t_len = len(temp_df.columns)
                # index = temp_df.index[temp_df.iloc[:, 0] == 'Well Name'][0]
                # temp_df = temp_df[index + 1:]
                if t_len == 6:
                    temp_df.columns = ['Well Name', 'Year', 'Month', 'Oil_(m³)', 'Gas_(10³m³)', 'Water_(m³)']
                elif t_len == 5:
                    temp_df['Well Name'] = np.NAN
                    temp_df.columns = ['Well Name', 'Year', 'Month', 'Oil_(m³)', 'Gas_(10³m³)', 'Water_(m³)']
                else:
                    temp_df.columns = ['Well Name', 'Year', 'Month', 'Total', 'Oil_(m³)', 'Gas_(10³m³)', 'Water_(m³)']
                all_tables = pd.concat([all_tables, temp_df])
                all_tables = all_tables[~all_tables['Well Name'].str.contains('Well Name')]
                print(all_tables)
    return all_tables
#
extraction(path)


