
from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sat_biblio_referencement import Base


__author__ = ["Clément Besnier <clem@clementbesnier.fr>"]


class PublishedWorksDB(Base):
    """
    :param id_:
    :param publication_type: 'bulletin', 'memoire'
    :param year:
    :param title:
    :param publication_type:

    """
    __tablename__ = "published_works"
    __table_args__ = {'sqlite_autoincrement': True}
    id_ = Column(Integer, primary_key=True)
    year = Column(String, nullable=False)
    title = Column(String, default="")
    publication_type = Column(String, default="")
    resources = Column(JSON, default="{}")

    def __repr__(self):
        return f"<PublishedWorksDB(id_={self.id_}, year={self.year}, " \
               f"publication_type={self.publication_type}," \
               f"resources={self.resources})>"


class PublishedWorkPagesDB(Base):
    """
    :param id_:
    :param published_work_id:
    :param text:
    :param page_number:
    :param publication_entry_id:

    """
    __tablename__ = "published_work_pages"
    __table_args__ = {'sqlite_autoincrement': True}
    id_ = Column(Integer, primary_key=True)
    published_work_id = Column(Integer, ForeignKey("published_works.id_"), nullable=False)
    text = Column(String, default="")
    page_number = Column(Integer, nullable=True)
    publication_entry_id = Column(Integer, ForeignKey("publication_entries.id_"), nullable=False)
    resources = Column(JSON, default="{}")

    def __repr__(self):
        return f"<PublishedWorkPagesDB(id_={self.id_}, published_work_id={self.published_work_id}," \
               f" text='{self.text}', page_number={self.page_number}, publication_entry_id={self.publication_entry_id}," \
               f" resources={self.resources}>"


class PublishedWorkArticlesDB(Base):
    """

    """
    __tablename__ = "published_work_articles"
    __table_args__ = {'sqlite_autoincrement': True}
    id_ = Column(Integer, primary_key=True)
    published_work_id = Column(Integer, ForeignKey("published_works.id_"), nullable=False)
    title = Column(String, default="vide")
    page_number_start = Column(Integer, nullable=False)
    page_number_end = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<PublishedWorkArticlesDB(id_={self.id_}, published_work_id={self.published_work_id}," \
               f" title='{self.title}', page_number_start={self.page_number_start}," \
               f" page_number_end={self.page_number_end})>"
