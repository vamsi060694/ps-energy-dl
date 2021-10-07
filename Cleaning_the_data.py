def reading_to_df(field_dir):
    field_dir_path = os.path.join(current_dir, field_dir)

    data = pd.read_csv(d_path, delimiter=',', header='infer')
    data_new.columns = data_new.columns.str.replace(' ', '_')
    data_new = data_new.rename(columns={'Unnamed:_3': 'Total'})
    data_new = data_new[data_new.Total != 'Yearly Total:']
    for columns in ['Well_Name', 'Year', 'Month']:
        data_new[columns] = data_new[columns].ffill()

    data_new.drop('Total', axis=1).dropna()


