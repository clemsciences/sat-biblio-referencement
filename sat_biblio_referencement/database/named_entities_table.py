from sqlalchemy import Column, Integer, String
from sat_biblio_referencement import Base


__author__ = ["Clément Besnier <clem@clementbesnier.fr>"]


class NamedEntitiesDB(Base):
    __tablename__ = "named_entities"
    __table_args__ = {'sqlite_autoincrement': True}
    id_ = Column(Integer, primary_key=True)
    name = Column(String)
    type_ = Column(String)
    standard_value = Column(String)
    description = Column(String)

    def __repr__(self):
        return f"<NamedEntitiesDB(id={self.id_}, name={self.name}, type_={self.type_}, " \
               f"standard_value={self.standard_value}, description={self.description})>"
