from sqlalchemy import create_engine
from databases import Database
from config import db_config

DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}' \
    .format(db_config.username, db_config.password, db_config.host, db_config.port, db_config.db_name)
database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
