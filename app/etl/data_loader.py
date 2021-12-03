import os
from app.etl import lookup_tables, production_data
from app.etl.downloading_the_data_files import downloading_src_files
from app.etl.extraction import extracted_data_files
from app.etl.transform_data import transforming_data
from app.utils.logging_init import init_logger
import json
import logging

logger = init_logger()

filters = os.getenv('REFERENCE').split(',')
folder_path = os.getenv('FOLDER_PATH')
data_path = os.path.join(f'{folder_path}/data_folder')


def data_insert():
    try:
        downloading_src_files(filters, data_path)
        for filter in filters:
            field = json.loads(os.getenv('FIELDS'))[filter]
            extracted_data = extracted_data_files(data_path, field)
            extracted_data['Field Name'] = field
            lookup_tables.update_fields_table(field)
            well_df = extracted_data[['Well Name', 'Field Name']]
            lookup_tables.update_well_table(well_df, field)
            extracted_data = extracted_data.drop(columns=['Field Name'])
            transformed_data = transforming_data(extracted_data)
            production_data.production_update_table(transformed_data)
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    data_insert()











