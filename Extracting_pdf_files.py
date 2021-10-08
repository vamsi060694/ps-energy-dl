import os

import camelot

#import pandas as pd


current_dir = os.getcwd()
print(current_dir)

field_dir_path = os.path.join(current_dir, 'hebron')
for path, dirs, files in os.walk(field_dir_path):
    for f in files:
        filename = os.path.join(path, f)
        with open(filename, 'r'):
            print(filename)
            tables = camelot.read_pdf(filename, pages='all',
                                      flavour='stream')
            print(type(tables))
            all_tables = tables.export(f'{myfile}.csv')
