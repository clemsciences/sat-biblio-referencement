
from sqlalchemy import Column, Integer, String, ForeignKey
from sat_biblio_referencement import Base


class PublishedWorksDB(Base):
    """
    :param id_:
    :param publication_type: 'bulletin', 'memoire'
    :param year:
    :param title:

    """
    __tablename__ = "published_works"
    __table_args__ = {'sqlite_autoincrement': True}
    id_ = Column(Integer, primary_key=True)
    year = Column(String, nullable=False)
    title = Column(String, default="")
    publication_type = Column(String, default="")


class PublishedWorkPagesDB(Base):
    """
    :param id_:
    :param bulletin_id:
    :param text:
    :
    """
    __tablename__ = "published_work_pages"
    __table_args__ = {'sqlite_autoincrement': True}
    id_ = Column(Integer, primary_key=True)
    published_work_id = Column(Integer, ForeignKey("published_works.id_"), nullable=False)
    text = Column(String, default="")
    page_number = Column(Integer, nullable=True)
    publication_entry_id = Column(Integer, ForeignKey("publication_entries.id_"), nullable=False)


class PublishedWorkArticlesDB(Base):
    __tablename__ = "published_work_articles"
    __table_args__ = {'sqlite_autoincrement': True}
    id_ = Column(Integer, primary_key=True)
    published_work_id = Column(Integer, ForeignKey("published_works.id_"), nullable=False)
    title = Column(String, default="vide")
    page_number_start = Column(Integer, nullable=False)
    page_number_end = Column(Integer, nullable=False)
