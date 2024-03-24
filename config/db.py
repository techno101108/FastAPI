from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:2001@localhost:3306/Book_store'
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping = True)
Base = declarative_base()
metadata = MetaData()
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
conn = engine.connect()

