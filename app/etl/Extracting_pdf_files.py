import os
#import camelot
directories = ['C:\workspace\ps-energy-dl\hebron_pdf',
               'C:\workspace\ps-energy-dl\hibernia_pdf',
               'C:\workspace\ps-energy-dl\methyst_north_pdf',
               'C:\workspace\ps-energy-dl\ova_terra_pdf',
               'C:\workspace\ps-energy-dl\white_ross_pdf']


# def read_pdf(dir_path):
#     field_dir_path = os.path.join(current_dir, dir_path)
#     for path, dirs, files in os.walk(field_dir_path):
#         for f in files:
#             filename = os.path.join(path, f)
#             #print(filename)
#             tables = camelot.read_pdf(filename, pages='all', flavor='stream', edge_tol=1000)
#             tables.export(f'{filename}.csv')
#             return tables
#
#
# folder_path = ['hibernia_pdf']
#
# for i in folder_path:
#     dir_path = os.path.join(current_dir, i)
#     print(dir_path)
#     read_pdf(dir_path)

current_dir = os.getcwd()
print(current_dir)


for directory in directories:
    field_dir_path = os.path.join(current_dir, directory)
    for path, dirs, files in os.walk(field_dir_path):
        for f in files:
            print(f)
            # filename = os.path.join(path, f)
            # print(filename)
            # tables = camelot.read_pdf(filename, pages='all', flavor='stream', edge_tol=1000)
            # tables.export(f'{filename}.csv')
