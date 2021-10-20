import os
from os.path import basename
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import datetime as dt
import json

load_dotenv()

filters = os.getenv('REFERENCE').split(',')


def all_years(data_path, field):
    answer = os.getenv('ALL_YEARS')
    if answer == 'yes':
        try:
            for source in sources:
                req = requests.get(f'{url}/{source}')
                with open(basename(f'{data_path}\\{field}\\{source}'), 'wb') as file:
                    file.write(req.content)
        except:
            print("Not able to download the required pdf files ")
    else:
        try:
            d = dt.date.today()
            for source in sources:
                if source.split('.')[-2][-4:] == str(d.year):
                    req = requests.get(f'{url}/{source}')
                    with open(basename(f'{data_path}\\{field}\\{source}'), 'wb') as file:
                        file.write(req.content)
        except:
            print("Not able to download the current year pdf files")


for filter in filters:

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
            print("Not able to extract the required pdf links from the given url")


    sources = pdf_links(f'https://www.cnlopb.ca/wp-content/uploads/{filter}')
    print(sources)

    folder_path = os.getenv('FOLDER_PATH')
    data_path = os.path.join(folder_path, "../../data_folder")


    def creating_directory(data_path):
        try:
            if not os.path.isdir(data_path):
                os.mkdir("../../data_folder")
                os.chdir(data_path)

        except:
            print("Not able to create the directory")


    creating_directory(data_path)

    fields = os.getenv('FOLDERS').split(',')
    field = json.loads(os.getenv('FIELDS'))[filter]
    # field = fields[filter]
    print("===>", field)

    def creating_fields(data_path, field):
        try:
            os.chdir(data_path)
            if not os.path.isdir(data_path + '\\' + field):
                os.mkdir(field)
            os.chdir(data_path + '\\' + field)
            print(">>", os.getcwd())
        except:
            print("Not able to create the respected folders")


    creating_fields(data_path, field)

    all_years(data_path, field)
    os.chdir(data_path)

