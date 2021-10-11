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
df = pd.concat([pd.read_csv(file, delimiter=',') for file in all_filenames])
df.columns = df.columns.str.replace(' ','_')
print(df[:25])
df= df[df.Well_Name != 'Yearly Total:']
print(df)
df = df.fillna(method='ffill')
#print(df[:50])
for columns in ['Well_Name', 'Year', 'Month']:
    df[columns] = df[columns].ffill()
print(df[:50])

#data_new.drop('Total', axis=1).dropna()
