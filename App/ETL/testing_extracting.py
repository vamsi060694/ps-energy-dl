import os
import camelot
import pandas as pd

path = 'C:\workspace\ps-energy-dl\data_folder\hibernia'

for path, dirs, files in os.walk(path):
    for f in files:
        # print(f)
        filename = os.path.join(path, f)
        tables = camelot.read_pdf(filename, pages='all', flavor='stream', edge_tol=1000)
        num = tables.n
        print(num)
        f_data = tables[0].df
        d_len = len(f_data.columns)
        index = f_data.index[f_data.iloc[:,0] == 'Well Name'][0]
        # print(index)
        f_data = f_data[index + 1:]

        if d_len == 6 or d_len == 5:
            f_data.columns = ['Well Name', 'Year', 'Month', 'Oil_(m³)', 'Gas_(10³m³)', 'Water_(m³)']
        else:
            f_data.columns = ['Well Name', 'Year', 'Month', 'Total', 'Oil_(m³)', 'Gas_(10³m³)', 'Water_(m³)']
        # print(f_data)
        all_tables = pd.DataFrame()
        for i in range(num):
            temp_df = (tables[i].df)
            all_tables = pd.concat([all_tables, f_data])


        if d_len == 7:
            all_tables = all_tables[~all_tables['Total'].str.contains('Yearly')]
            all_tables = all_tables.drop('Total', axis=1)
        else:
            all_tables = all_tables[~all_tables['Month'].str.contains('Yearly')]
        all_tables['Month'] = '01' + '-' + all_tables['Month'] + '-' + all_tables['Year']
        new_tables = all_tables.drop(columns='Year', axis=1)
        new_tables = new_tables.rename(
            columns={'Well Name': 'well_name', 'Month': 'month', 'Oil_(m³)': 'oil (m3)',
                     'Gas_(10³m³)': 'gas (103m3)',
                     'Water_(m³)': 'water (m3)'}, inplace=False)
        new_tables1 = new_tables.fillna(method='ffill')
        print(new_tables1)









