import os
from os.path import basename
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()

filters = os.getenv('REFERENCE').split(',')
for filter in filters:

    url = f'https://www.cnlopb.ca/wp-content/uploads/{filter}'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    sources = []
    for link in soup.find_all('a'):
        if 'pdf' in link['href']:
            sources.append(link.get('href'))

    fields = os.environ["FOLDERS"].split(',')
    data_path = os.getenv('FOLDER_PATH')
    for field in fields:
        os.mkdir(f'{data_path}\\{field}')

    for source in sources:
        req = requests.get(f'{url}/{source}')
        with open(basename(r'{data_path}\\{field}\\{source}'), 'wb') as file:
            file.write(req.content)
