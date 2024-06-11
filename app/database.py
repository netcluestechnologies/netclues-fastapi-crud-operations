from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://user:password@host:port/database_name" # Replace with your database connection deatils

engine = create_engine(DATABASE_URL)

Base = declarative_base()
sessionLocal = sessionmaker(bind=engine)
