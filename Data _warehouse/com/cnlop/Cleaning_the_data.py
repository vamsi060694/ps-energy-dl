import os
import glob
import pandas as pd

cwd = os.getcwd()
path = 'C:\workspace\ps-energy-dl\HIBERNIA'
os.chdir(path)
file_extension = '.csv'
all_filenames = list([i for i in glob.glob(f'*{file_extension}')])


df = [pd.read_csv(file, delimiter='\t',encoding='UTF-8') for file in all_filenames]
table = df[1]
