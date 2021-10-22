



def all_years(data_path, field):
    answer = os.getenv('ALL_YEARS')

    if answer == 'yes':
        try:
            for source in sources:
                req = requests.get(f'{url}/{source}')
                with open(basename(f'{data_path}\\{field}\\{source}'), 'wb') as file:
                    file.write(req.content)
        except:
            print("Not able to download required pdf files")

    else:
        try:
            d = dt.date.today()
            for source in sources:
                if source.split('.')[-2][-4:] == str(d.year):
                    req = requests.get(f'{url}/{source}')
                    with open(basename(f'{data_path}\\{field}\\{source}'), 'wb') as file:
                        file.write(req.content)
        except:
            print("Not able to download current year files")


def pdf_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        websites = []
        for link in soup.find_all('a'):
            if 'pdf' in link['href']:
                websites.append(link.get('href'))
        return websites
    except:
        print("Not able to extract the requird pdf files")


sources = pdf_links(f'https://www.cnlopb.ca/wp-content/uploads/{filter}')
print(sources)


def creating_folder(data_path):
    try:
        if not os.path.isdir(data_path):
            os.mkdir('../../data_folder')
    except:
        print("Not able to create data folder")


def creating_fields(data_path, field):
    try:
        if not os.path.isdir(data_path + '\\' + field):
            os.mkdir(field)
        os.chdir(data_path + '\\' + field)
        print(">>", os.getcwd())
    except:
        print("Not able to create respective field folders")


def providing_path(filters):
    for filter in filters:
        try:
            sources = pdf_links(f'https://www.cnlopb.ca/wp-content/uploads/{filter}')
            print(sources)

            folder_path = os.getenv('FOLDER_PATH')
            data_path = os.path.join(folder_path + '\\' + '../../data_folder')

            creating_folder(data_path)

            fields = os.getenv('FOLDERS').split(',')
            print(fields)

            field = json.loads(os.getenv('FIELDS'))[filter]
            # field = fields[filter]
            print("===>", field)
            os.chdir(data_path)
            creating_fields(data_path, field)
            all_years(data_path, field)
            os.chdir(data_path)
        except:
            print("Not able to extract the pdf links and provide path")


def extraction(data_path):
    global all_tables
    for path, dirs, files in os.walk(data_path):
        for file in files:
            # print(file)
            filename = os.path.join(path, file)
            tables = camelot.read_pdf(filename, pages='all', flavor='stream', edge_tol=1000)
            num = tables.n
            logger.info(num)
            all_tables = pd.DataFrame()
            for i in range(num):
                temp_df = tables[i].df
                t_len = len(temp_df.columns)
                try:
                    # index = temp_df.index[temp_df.iloc[:, 0] == 'Well Name'][0]
                    # temp_df = temp_df[index + 1:]
                    if t_len == 6:
                        temp_df.columns = ['Well Name', 'Year', 'Month', 'Oil_(m³)', 'Gas_(10³m³)', 'Water_(m³)']
                    elif t_len == 5:
                        temp_df['Well Name'] = np.NAN
                        temp_df.columns = ['Well Name', 'Year', 'Month', 'Oil_(m³)', 'Gas_(10³m³)', 'Water_(m³)']
                    else:
                        temp_df.columns = ['Well Name', 'Year', 'Month', 'Total', 'Oil_(m³)', 'Gas_(10³m³)',
                                           'Water_(m³)']
                except:
                    print('Not able to change columns')
                    all_tables = pd.concat([all_tables, temp_df])
                    all_tables = all_tables[~all_tables['Well Name'].str.contains('Well Name')]
                    print(all_tables)
                return all_tables

new_tables = extraction(data_path)


def transforming_data(data_path):
    try:
        sample_data = pd.read_csv(data_path, header=0, sep=',')
        s_data = sample_data.rename(
            columns={'Oil (m3)': 'crude_oil (m3)', 'Gas (103m3)': 'natural_gas (km3)', 'Water (m3)': 'other (m3)',
                     'value': 'Value'}, inplace=False)
        transpose_data = s_data.melt(['well_name', 'month'], var_name='Comodity', value_name='Value')
        # transpose_data['energy'] = transpose_data['Comodity'].str.split(' ', 0).str[0]
        transpose_data[['energy', 'units']] = transpose_data['Comodity'].str.split('(', expand=True)
        transpose_data['units'] = transpose_data['units'].str.replace('[)]', '', regex=True)

        return print(transpose_data)
    except:
        print("Not able to process the data")

def cleaning(new_tables):
    all_columns = new_tables.columns
    for columns in ['Well Name', 'Year', 'Month', 'Oil (m³)', 'Gas (10³m³)', 'Water (m³)']:
        new_tables[columns] = new_tables[columns].replace('', np.NAN)
        for columns in ['Well Name', 'Year', 'Month']:
            new_tables[columns] = new_tables[columns].fillna(method='ffill')
    return new_tables