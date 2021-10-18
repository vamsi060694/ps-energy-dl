import os
import camelot
import pandas as pd
path = 'C:\workspace\ps-energy-dl\data_folder\hibernia'
for path, dirs, files in os.walk(path ):
    for f in files:
        #print(f)
        filename = os.path.join(path, f)
        #print(filename)
        tables = camelot.read_pdf(filename, pages='all', flavor='stream',edge_tol=1000)
        num = tables.n
        f_data = tables[0].df
        d_len = len(f_data.columns)
        index = f_data.index[f_data.iloc[:,0] == 'Well Name'][0]
        f_data = f_data[index + 1:]
        if d_len == 6:
            f_data.columns = ['Well Name', 'Year', 'Month', 'Oil_(m³)', 'Gas_(10³m³)', 'Water_(m³)']
        else:
            f_data.columns = ['Well Name', 'Year', 'Month', 'Total', 'Oil_(m³)', 'Gas_(10³m³)', 'Water_(m³)']

            for i in range(1,num):
                temp_df = tables[i].df
                d_len = len(temp_df.columns)
                if d_len == 6:
                    temp_df.columns = ['Well Name','Year','Month','Oil_(m³)','Gas_(10³m³)','Water_(m³)']
                else:
                    temp_df.columns = ['Well Name', 'Year', 'Month', 'Total', 'Oil_(m³)', 'Gas_(10³m³)', 'Water_(m³)']

                f_data = pd.concat([f_data,temp_df])
                print(f_data[:50])









        # all_tables = pd.DataFrame()
        # for i in range(1,n):
        #     temp_df = (tables[i].df)
        #     all_tables = pd.concat([all_tables,temp_df])
        # print(all_tables)
        # # print(type(tables[0]))
        # # # tables.export(f'{filename}.csv')