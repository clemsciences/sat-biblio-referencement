import os

PACKDIR = os.path.abspath(os.path.dirname(__file__))


from sqlalchemy.orm import declarative_base

Base = declarative_base()

DATABASE_DIRECTORY = os.path.join(PACKDIR, "database")
