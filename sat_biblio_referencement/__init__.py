import os

PACKDIR = os.path.abspath(os.path.dirname(__file__))


from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

DATABASE_DIRECTORY = os.path.join(PACKDIR, "database")
TABLE_PUBLICATION_2004_FILENAME = "publication_table_2004.db"
