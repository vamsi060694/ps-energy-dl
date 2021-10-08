import os
import glob
import pandas as pd

cwd = os.getcwd()
print(cwd)
path = 'C:\workspace\ps-energy-dl\HIBERNIA'
os.chdir(path)
file_extension = '.csv'
all_filenames = list([i for i in glob.glob(f'*{file_extension}')])
print(all_filenames)

df = [pd.read_csv(file, delimiter=',') for file in all_filenames]
print(df[1:])