

import os

from sat_biblio_referencement import PACKDIR
from sat_biblio_referencement.data.info_extraction import Extractor
from sat_biblio_referencement.data.readers import read_text, split_page
from sat_biblio_referencement.database.database_manager import DatabaseManager
from sat_biblio_referencement.data.published_work_data import *
from sat_biblio_referencement.data.publication_entries_data import *


DIRECTORY_NAME = os.path.join(PACKDIR, "experiments", "2022-11-19", "text")

filenames = {int(i.split("_")[0]): i for i in os.listdir(DIRECTORY_NAME)}
sorted_filenames = []
for i in range(1, len(filenames)+1):
    sorted_filenames.append(filenames[i])

pages = []
for filename in sorted_filenames:
    text = read_text(DIRECTORY_NAME, filename)
    pages.extend([split_page(page) for page in text.split("\n\n") if page])


dbm = DatabaseManager(in_memory=False, is_echo=False)
dbm.prepare()
session = dbm.get_session()
for i, page in enumerate(pages):
    for entry in page:
        # print(entry)
        named_entity = Extractor.extract_named_entity(entry)
        named_entity_db = session.query(NamedEntitiesDB).filter_by(name=named_entity).one_or_none()
        if not named_entity_db:
            named_entity_db = NamedEntitiesData.from_data_to_db(
                dict(name=named_entity,
                     type_="",
                     description="",
                     standard_value=named_entity)
            )
            session.add(named_entity_db)
            session.commit()
        publication_entry_db = session.query(PublicationEntriesDB).filter_by(text=entry).one_or_none()
        if not publication_entry_db:
            publication_entry_db = PublicationEntriesData.from_data_to_db(dict(
                text=entry,
                named_entity_id=named_entity_db.id_
            ))
            session.add(publication_entry_db)
            session.commit()
        citations = Extractor.extract_citation(entry)
        for citation in citations:
            citation_year = citation.get("year", "")
            citation_work = citation.get("work", "")
            published_entry_db = session.query(PublishedWorksDB).filter_by(
                year=citation_year,
                publication_type=citation_work).one_or_none()
            if not published_entry_db:
                published_entry_db = PublishedWorksData.from_data_to_db(dict(
                    year=citation_year,
                    title="",
                    publication_type=citation_work))
                session.add(published_entry_db)
                session.commit()
            citation_page = citation.get("page")
            published_work_page_db = session.query(PublishedWorkPagesDB).filter_by(
                page_number=citation_page,
                published_work_id=published_entry_db.id_,
                publication_entry_id=publication_entry_db.id_)
            if not published_work_page_db:
                published_work_page_db = PublishedWorkPagesData.from_data_to_db(dict(
                    text="",
                    page_number=citation_page,
                    published_work_id=published_entry_db.id_,
                    publication_entry_id=publication_entry_db.id_,
                ))
                session.add(published_work_page_db)
                session.commit()
        # if citations:
        #     print(i+1, Extractor.extract_named_entity(entry), citations)




