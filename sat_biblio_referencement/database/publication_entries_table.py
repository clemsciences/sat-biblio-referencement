from sqlalchemy import Column, Integer, String, ForeignKey
from sat_biblio_referencement import Base


class PublicationEntriesDB(Base):
    __tablename__ = "publication_entries"
    __table_args__ = {'sqlite_autoincrement': True}
    id_ = Column(Integer, primary_key=True)
    text = Column(String)
    named_entity_id = Column(Integer, ForeignKey("named_entities.id_"), nullable=False)

    def __repr__(self):
        return f"<PublicationEntriesDB>(id_={self.id_}, text='{self.text}', named_entitiy_id={self.named_entity_id})"


