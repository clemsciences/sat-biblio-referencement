from sqlalchemy import Column, Integer, String
from sat_biblio_referencement import Base


class NamedEntitiesDB(Base):
    __tablename__ = "named_entities"
    __table_args__ = {'sqlite_autoincrement': True}
    id_ = Column(Integer, primary_key=True)
    name = Column(String)
    type_ = Column(String)
    standard_value = Column(String)
    description = Column(String)
