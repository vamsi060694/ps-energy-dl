#import camelot
import os
from app.utils.logging_init import init_logger
from dotenv import load_dotenv

logger = init_logger()

load_dotenv()

folder_path = os.getenv('FOLDER_PATH')
logging.info(folder_path)
data_path = os.path.join(folder_path,'data_folder')
logging.info(data_path)

directories = os.listdir(data_path)
logger.info(directories)

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
