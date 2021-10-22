import os
from os.path import basename
import logging
import camelot
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import datetime as dt
import json
import sqlalchemy
import pandas as pd
from app.etl.logging_init import init_logger
from app.utils.etl_utils import etl_utils as et


load_dotenv()

logger = init_logger()


filters = os.getenv('REFERENCE').split(',')
folder_path = os.getenv('FOLDER_PATH')
data_path = os.path.join(folder_path + '\\' + '../../data_folder')
fields = os.getenv('FOLDERS').split(',')
field = json.loads(os.getenv('FIELDS'))[filter]
et.all_years(data_path, field)

et.providing_path(filters)
new_tables = et.extraction(data_path)

et.transforming_data(data_path)
