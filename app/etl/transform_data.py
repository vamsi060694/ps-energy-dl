import pandas as pd
from app.utils.logging_init import init_logger
from app.etl import lookup_tables
import logging
logger = init_logger()


def transforming_data(cleaned_data):
    try:
        units_table = lookup_tables.get_unit_of_measure()
        energy_product_table = lookup_tables.get_energy_units()
        well_lookup_df = lookup_tables.get_all_wellids()
        cleaned_data.columns = ['well_name', 'month', 'crude_oil(m3)', 'natural_gas(km3)', 'other(m3)']
        transpose_data = pd.melt(cleaned_data, id_vars=['well_name', 'month'],
                                 value_vars=['crude_oil(m3)', 'natural_gas(km3)', 'other(m3)'], var_name='Comodity')
        transpose_data[['energy', 'units']] = transpose_data['Comodity'].str.split('(', expand=True)
        transpose_data['units'] = transpose_data['units'].str.replace('[)]', '', regex=True)
        transpose_data['energy_product_id'] = transpose_data.energy.str.lower().map(energy_product_table.set_index('energy_product')['id'])
        transpose_data['unit_of_measure_id'] = transpose_data.units.str.lower().map(units_table.set_index('uom')['unit_of_measure_id'])
        transpose_data['well_id'] = transpose_data.well_name.map(well_lookup_df.set_index('well_name')['id'])
        transpose_data = transpose_data.drop(['energy', 'units', 'Comodity', 'well_name'], axis=1)
        logger.info("Able to transform the data in the required format")
        return transpose_data
    except Exception as e:
        logging.error(e)
