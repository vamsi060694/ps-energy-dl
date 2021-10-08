import os
import glob
import pandas as pd

cwd = os.getcwd()
path = '/HIBERNIA'
os.chdir(path)
file_extension = '.csv'
all_filenames = list([i for i in glob.glob(f'*{file_extension}')])
print(all_filenames)

df = [pd.read_csv(file, delimiter='\t',encoding='UTF-16') for file in all_filenames]
camel