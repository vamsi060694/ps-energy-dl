import pandas as pd
import logging

units_data = pd.read_csv(r'C:\Users\siri sagi\PycharmProjects\ps-energy-dl\units.csv', header=0, sep=',')
product_data = pd.read_csv(r'C:\Users\siri sagi\PycharmProjects\ps-energy-dl\eneryproduct.csv', header=0, sep=',')


def transforming_data(transform_path, units_data, product_data):
    try:
        sample_data = pd.read_csv(transform_path, header=0, sep=',')
        transpose_data = sample_data.melt(['Well Name', 'Month'], value_vars=['Oil_(m³)', 'Gas_(10³m³)', 'Water_(m³)'], var_name='Comodity', value_name='Value')
        # transpose_data['energy'] = transpose_data['Comodity'].str.split(' ', 0).str[0]
        transpose_data[['energy', 'units']] = transpose_data['Comodity'].str.split('(', expand=True)
        transpose_data['energy'] = transpose_data['energy'].str.replace('[_]', '', regex=True)
        transpose_data['units'] = transpose_data['units'].str.replace('[)]', '', regex=True)
        transpose_data = transpose_data.replace(transpose_data['energy'], product_data['ID'])
        transpose_data = transpose_data.replace(transpose_data['energy'], units_data['ID'])
        return print(transpose_data)
    except Exception as e:
        logging.error(e)


transforming_data(r'C:\Users\siri sagi\PycharmProjects\ps-energy-dl\data_folder\csv_file.csv', units_data, product_data)