import camelot

# import sqlite3

# import pandas as pd


current_dir = os.getcwd()


# print(current_dir)


def read_pdf(dir_path):
    field_dir_path = os.path.join(current_dir, dir_path)
    for path, dirs, files in os.walk(field_dir_path):
        for f in files:
            filename = os.path.join(path, f)
            #print(filename)
            tables = camelot.read_pdf(filename, pages='all', flavor='stream', edge_tol=1000)
            tables.export(f'{filename}.csv')
            return tables


folder_path = ['hibernia_pdf']

for i in folder_path:
    dir_path = os.path.join(current_dir, i)
    print(dir_path)
    read_pdf(dir_path)
