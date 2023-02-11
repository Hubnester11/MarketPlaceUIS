from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:12345@localhost:5432/MarketPlaceUIS"
engine= create_engine(SQLALCHEMY_DATABASE_URL)
SESIONLOCAL = sessionmaker(bind=engine, autocommit=false, autoflush=false)