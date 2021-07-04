from sqlalchemy import create_engine
from databases import Database

DATABASE_URL = 'postgresql://test_user:test_password@127.0.0.1:8080/test_db'
database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
