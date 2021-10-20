import os
import camelot
import numpy as np
import pandas as pd

path = 'C:\workspace\ps-energy-dl\data_folder\hibernia'


def extraction(path):
    for path, dirs, files in os.walk(path):
        for f in files:
            #print(f)
            filename = os.path.join(path, f)
            tables = camelot.read_pdf(filename, pages='all', flavor='stream', edge_tol=1000)
            num = tables.n
            #print(num)
            f_data = tables[0].df
            d_len = len(f_data.columns)
            index = f_data.index[f_data.iloc[:,0] == 'Well Name'][0]
            # print(index)
            f_data = f_data[index + 1:]
            if d_len == 6 or d_len == 5:
                f_data.columns = ['Well Name', 'Year', 'Month', 'Oil_(m³)', 'Gas_(10³m³)', 'Water_(m³)']
            else:
                f_data.columns = ['Well Name', 'Year', 'Month', 'Total', 'Oil_(m³)', 'Gas_(10³m³)', 'Water_(m³)']
            for i in range(1,num):
                temp_df = tables[i].df
                index = temp_df.index[temp_df.iloc[:,0] == 'Well Name'][0]
                temp_df = temp_df[index + 1:]
            all_tables = pd.DataFrame()
            for i in range(num):
                temp_df = (tables[i].df)
                all_tables = pd.concat([all_tables, temp_df])
                print(all_tables)


            # if d_len == 7:
            #     all_tables = all_tables[~all_tables['Total'].str.contains('Yearly')]
            #     all_tables = all_tables.drop('Total', axis=1)
            # else:
            #     all_tables = all_tables[~all_tables['Month'].str.contains('Yearly')]
            # print(all_tables)
            #
            # for columns in ['Well Name', 'Year', 'Month','Oil_(m³)','Gas_(10³m³)','Water_(m³)']:
            #     all_tables[columns] = all_tables[columns].replace('', np.NaN)
            #
            # for columns in ['Well Name', 'Year', 'Month']:
            #     all_tables[columns] = all_tables[columns].fillna(method='ffill')
            # print(all_tables[:55])
            # # df1 = all_tables.dropna()
            # # print(df1)
        #
        # return num


extraction(path)
