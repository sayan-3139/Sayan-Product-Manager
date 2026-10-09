from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url =  "postgresql+psycopg://postgres:Sayan%4012345@localhost:5432/Sayan"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
