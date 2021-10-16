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
        for source in sources:
            req = requests.get(f'{url}/{source}')
            with open(basename(f'{data_path}\\{field}\\{source}'), 'wb') as file:
                file.write(req.content)

    else:

        d = dt.date.today()

        for source in sources:
            if source.split('.')[-2][-4:] == str(d.year):
                req = requests.get(f'{url}/{source}')
                with open(basename(f'{data_path}\\{field}\\{source}'), 'wb') as file:
                    file.write(req.content)


for filter in filters:

    url = f'https://www.cnlopb.ca/wp-content/uploads/{filter}'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    sources = []
    for link in soup.find_all('a'):
        if 'pdf' in link['href']:
            sources.append(link.get('href'))

    print(sources)

    data_path = os.getenv('FOLDER_PATH')
    fields = os.getenv('FOLDERS').split(',')
    print(fields)

    field = json.loads(os.getenv('FIELDS'))[filter]
    # field = fields[filter]
    print("===>", field)
    os.chdir(data_path)
    if not os.path.isdir(data_path + '\\' + field):
        os.mkdir(field)
    os.chdir(data_path + '\\' + field)
    print(">>", os.getcwd())

    all_years(data_path, field)
    os.chdir(data_path)
