import camelot
import os

current_dir = os.getcwd()
#for site in websites:
    #website_year = site.split('/')[-1][-8:-4]


def extract_tables(field_dir,year):
    field_path = os.path.join(current_dir,field_dir)
    for i in open(field_path,'r'):
        if year == i.split('/')[-1][-8:-4]:
            file_by_year = os.path.join(field_path, i)
            pdf = open(file_by_year, 'r')
            table = camelot.read_pdf(pdf, pages='all', flavour='stream')
            all_tables = table.export(f'{pdf}.csv')
            return all_tables

extract_tables('heb','2017')