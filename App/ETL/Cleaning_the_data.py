import os
import glob
import pandas as pd

cwd = os.getcwd()
print(cwd)
path = 'C:\workspace\ps-energy-dl\hebron'
os.chdir(path)
file_extension = '.csv'
all_filenames = list([i for i in glob.glob(f'*{file_extension}')])
#print(all_filenames)
df = pd.concat([pd.read_csv(file, delimiter=',',header='infer') for file in all_filenames])
df.columns = df.columns.str.replace(' ', '_')
df1 = df.rename(columns={'Well_Name':'well_name','Year':'year','Month':'month','Oil_(m³)':'oil_(m3)','Gas_(10³m³)':'gas_(103m3)','Water_(m³)':'water_m3'})
df1 = df1[df.Well_Name != 'Yearly Total:']
for columns in ['well_name', 'year', 'month']:
    df1[columns] = df1[columns].ffill()
print(df1[:50])


# #data_new.drop('Total', axis=1).dropna()
#'Well_Name':'well_name','Year':'year','Month':'month'