import os
from os.path import basename
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import datetime as dt
import json
import logging
from app.utils.logging_init import init_logger

logger = init_logger()
load_dotenv()


def all_years(data_path, field, sources, url):
    answer = os.getenv('ALL_YEARS')

    if answer == 'yes':
        try:
            for source in sources:
                req = requests.get(f'{url}/{source}')
                with open(basename(f'{data_path}//{field}//{source}'), 'wb') as file:
                    file.write(req.content)
            logger.info("Able to download the required files of all the years")

        except Exception as e:
            logging.error(e)

    else:
        try:
            d = dt.date.today()
            for source in sources:
                if source.split('.')[-2][-4:] == str(d.year):
                    req = requests.get(f'{url}/{source}')
                    with open(basename(f'{data_path}//{field}//{source}'), 'wb') as file:
                        file.write(req.content)
            logger.info("Able to download the files of the current year")
        except Exception as e:
            logging.error(e)


def pdf_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        websites = []
        for link in soup.find_all('a'):
            if 'pdf' in link['href']:
                websites.append(link.get('href'))
            logger.info("Able to extract the required pdf file links")
        return websites
    except Exception as e:
        logging.error(e)


def creating_base_path(data_path):
    try:
        if not os.path.isdir(data_path):
            os.mkdir(f'{data_path}')
        logger.info("Able to create the data folder")
    except Exception as e:
        logging.error(e)


def creating_fields_name_path(data_path, field):
    try:
        if not os.path.isdir(f'{data_path}/{field}'):
            os.mkdir(field)
        os.chdir(data_path + '//' + field)
        logger.info("Able to create the folders with field names")
    except Exception as e:
        logging.error(e)


def downloading_src_files(filters, data_path):
    for filter in filters:
        try:
            url = f'https://www.cnlopb.ca/wp-content/uploads/{filter}'

            sources = pdf_links(url)
            creating_base_path(data_path)

            field = json.loads(os.getenv('FIELDS'))[filter]
            # field = fields[filter]
            os.chdir(data_path)

            creating_fields_name_path(data_path, field)
            all_years(data_path, field, sources, url)
            os.chdir(data_path)
            logger.info("Able to download the required pdf files")
        except Exception as e:
            logging.error(e)

