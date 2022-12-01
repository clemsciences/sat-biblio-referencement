import os

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

from sat_biblio_referencement.database import *


class DatabaseManager:
    def __init__(self, in_memory, is_echo, path=""):
        self.path = path
        self.engine = None
        self.in_memory = in_memory
        self.is_echo = is_echo

    def create_database(self):
        if self.in_memory:
            self.engine = create_engine("sqlite:///:memory:", echo=self.is_echo)
        else:
            self.engine = create_engine(f"sqlite:///{self.path}", echo=self.is_echo)
        self.connection = self.engine.connect()
        self.metadata = MetaData()

    def add_tables(self):
        self.metadata.create_all(self.engine, tables=[
            PublishedWorksDB.__table__,
            NamedEntitiesDB.__table__,
            PublishedWorkArticlesDB.__table__,
            PublishedWorkPagesDB.__table__,
            PublicationEntriesDB.__table__
        ])

    def prepare(self):
        self.create_database()
        self.add_tables()

    def get_session(self):
        return sessionmaker(bind=self.engine)()


