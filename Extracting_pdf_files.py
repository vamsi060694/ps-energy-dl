import camelot
import os
import pandas as pd

current_dir = os.getcwd()


# for site in websites:
# website_year = site.split('/')[-1][-8:-4]


def extract_tables(field_dir):
    field_dir_path = os.path.join(current_dir, field_dir)
    for year in open(field_dir_path, 'r'):
        file_by_year = os.path.join(field_dir_path, year)
        pdf = open(file_by_year, 'r')
        tables = camelot.read_pdf(pdf, pages='all', flavour='stream')
        all_tables = tables.export(f'{pdf}.csv')
        return all_tables


extract_tables('hebron')

d_path = 'hib_oil_2021.pdf-page-1-table-1.csv'


def reading_to_df(field_dir):
    field_dir_path = os.path.join(current_dir, field_dir)

    data = pd.read_csv(d_path, delimiter=',', header='infer')
    data.fillna({'Well Name': 'HIB-B-016-001', 'Year': 2021, 'Month': 0}).dropna(). \
        rename(columns={'Well Name': 'Well_names'})
