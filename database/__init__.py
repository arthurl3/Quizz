from config import DEBUG
from logger import LOGGER
from .connect import session, engine
from .clean_up import cleanup_data
from .init_db import fill_database
import app.models

def init_script():
    """Run all scripts."""
    if DEBUG:

        # OPTIONAL: Reset table data after each run
        LOGGER.info("----------------------------------------------------")
        LOGGER.info("Purging all created data...")
        cleanup_data()


        LOGGER.info("----------------------------------------------------")
        LOGGER.info("Fill database with test rows")
        fill_database()

