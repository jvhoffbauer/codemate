from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.gear.sumar.config import SUMAR_DATABASE_URL


engine = create_engine(SUMAR_DATABASE_URL)

SessionLocalSumar = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

meta = MetaData()
