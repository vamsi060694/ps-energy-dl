import os
import camelot
import numpy as np
import pandas as pd

path = 'C:\workspace\ps-energy-dl\data_folder\hibernia'


for path, dirs, files in os.walk(path):
    for f in files:
        # print(f)
        filename = os.path.join(path, f)
        tables = camelot.read_pdf(filename, pages='all', flavor='stream', edge_tol=1000)
        #print(tables)
        n = tables.n
        #print(num)
        data = tables[0].df
        d_len = len(data.columns)
        index = data.index[data.iloc[:, 0] == 'Well Name'][0]
        data = data[index + 1:]
        if d_len == 6:
            data.columns = ['Well Name', 'Year', 'Month', 'Oil_(m³)', 'Gas_(10³m³)', 'Water_(m³)']
        else:
            data.columns = ['Well Name', 'Year', 'Month', 'Total', 'Oil_(m³)', 'Gas_(10³m³)', 'Water_(m³)']
        # print(f_data)

        for i in range(n):
            temp = tables[i].df
            d_len =len(temp.columns)
            try:
                index = temp.index[temp.iloc[:,0] == 'Well Name'][0]
                temp = temp[index + 1:]
                if d_len == 6:
                    temp.columns = ['Well Name', 'Year', 'Month', 'Oil_(m³)', 'Gas_(10³m³)', 'Water_(m³)']
                else:
                    temp.columns =  ['Well Name', 'Year', 'Month', 'Total', 'Oil_(m³)', 'Gas_(10³m³)', 'Water_(m³)']
            except:
                if d_len == 6 or d_len == 5:
                    if d_len == 6:
                        temp.columns = ['Well Name', 'Year', 'Month', 'Oil_(m³)', 'Gas_(10³m³)', 'Water_(m³)']
                    else:
                        temp['Well Name'] = ''
                        temp.columns = ['Year','Month','Oil_(m³)', 'Gas_(10³m³)', 'Water_(m³)','Well Name']
                else:
                    temp.columns = ['Well Name', 'Year', 'Month', 'Total', 'Oil_(m³)', 'Gas_(10³m³)', 'Water_(m³)']

        all_data = pd.concat([data,temp])
        print(all_data)
























            # print()
        # all_tables = pd.DataFrame()
        # i=0
        # for i in range(1,num):
        #     df = tables[i].df
        #     t_len = len(df.columns)
        #     idex = df.index[df.iloc[:,0] == ['Well Name'][0]
        #     df = df[index + 1:]
        #     all_tables = pd.concat([all_tables, df])
        # print(all_tables[:50])


        # if d_len == 7:
        #     all_tables = all_tables[~all_tables['Total'].str.contains('Yearly')]
        #     all_tables = all_tables.drop('Total', axis=1)
        # else:
        #     all_tables = all_tables[~all_tables['Month'].str.contains('Yearly')]
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
        #
        # #print(all_tables)
        # #     all_tables[columns] = all_tables[columns].fillna(method='ffill')
        # #     all_tables['Year'] = all_tables['Year'].fillna(method='ffill')
        # # print(all_tables)
        #
        #
        #
        #
        #
        # # #print(all_tables)
        # # new_df = all_tables.fillna(0)
        # # print(new_df)
        # # # all_tables['Month'] = '01' + '-' + all_tables['Month'] + '-' + all_tables['Year']
        # # # print(all_tables)
        # # # #new_tables = all_tables.drop(columns='Year', axis=1)
        # # # #new_tables = new_tables.rename(
