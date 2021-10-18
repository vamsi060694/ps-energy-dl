#import camelot
import os
import logging
from dotenv import load_dotenv

logging.basicConfig(filename='extraction.log',level=logging.INFO,
                    format='%(asctime)s %(message)s')


load_dotenv()

folder_path = os.getenv('FOLDER_PATH')
print(folder_path)
data_path = os.path.join(folder_path,'data_folder')
print(data_path)

directories = os.listdir(data_path)
logging.info(directories)

# def extract(directories, data_path):
#     for directory in directories:
#         field_dir_path = os.path.join(data_path, directory)
#         print(field_dir_path)
#         for path, dirs, files in os.walk(field_dir_path):
#             for f in files:
#                 print(f)
#                 filename = os.path.join(path, f)
#                 print(filename)
#                 tables = camelot.read_pdf(filename, pages='all', flavor='stream')
#                 tables.export(f'{filename}.csv')
#
#
# extract(directories, data_path)

























# path = '/app/etl/testing/data_folder\hibernia'
# os.chdir(path)
# for path, dirs, files in os.walk(path):
#     for f in files:
#         print(f)
#         filename = os.path.join(path, f)
#         print(filename)
#         tables = camelot.read_pdf(filename, pages='all', flavor='stream')
#         tables.export(f'{filename}.csv')

# def extract(directories, data_path):
#     for directory in directories:
#         field_dir_path = os.path.join(data_path, directory)
#         print(field_dir_path)
#         for path, dirs, files in os.walk(field_dir_path):
#             for f in files:
#                 print(f)
#                 filename = os.path.join(path, f)
#                 print(filename)
#                 tables = camelot.read_pdf(filename, pages='all', flavor='stream')
#                 tables.export(f'{filename}.csv')
#
#
# extract(directories, data_path)
