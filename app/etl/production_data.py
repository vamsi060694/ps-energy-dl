from app.utils.db_connectivity import db_connection
from app.utils.logging_init import init_logger
import sqlalchemy

logger = init_logger()


def production_update_table(transpose_data):
    # updating production lookup table
    try:
        conn = db_connection()
        transpose_data.to_sql(
            'tbl_cnlopb_production',
            con=conn,
            if_exists='append',
            method='multi',
            index=False,
            schema='collections',
            dtype={"well_id": sqlalchemy.types.INT,
                   "energy_product_id": sqlalchemy.types.INT,
                   "unit_of_measure_id": sqlalchemy.types.INT,
                   "month": sqlalchemy.types.DATE,
                   "value": sqlalchemy.types.FLOAT(),
                   }
        )
        logger.info("successfully inserted data")
    except Exception as e:
        logger.error(e)
