import os
from typing import List, Union

from sqlalchemy.orm import Session

from sat_biblio_referencement import DATABASE_DIRECTORY, TABLE_PUBLICATION_2004_FILENAME
from sat_biblio_referencement.data.publication_entries_data import NamedEntitiesData
from sat_biblio_referencement.data.published_work_data import PublishedWorkPagesData, PublishedWorksData
from sat_biblio_referencement.database import NamedEntitiesDB, PublicationEntriesDB, PublishedWorkPagesDB, PublishedWorksDB
from sat_biblio_referencement.database.database_manager import DatabaseManager


__author__ = ["Clément Besnier <clem@clementbesnier.fr>"]


class SearchManager:

    @staticmethod
    def search_near_named_entities(db_session: Session, query: str) -> List:
        results = SearchManager.search_approximate(db_session, query)
        return [ne_db.standard_value for ne_db in results]

    @staticmethod
    def search(db_session: Session, query: str) -> List[NamedEntitiesDB]:
        """
        >>> db = DatabaseManager(False, False, os.path.join(DATABASE_DIRECTORY, TABLE_PUBLICATION_2004_FILENAME))
        >>> db.prepare()
        >>> SearchManager.search(Session(db.engine), "Bléré")
        [<NamedEntitiesDB(id=633, name=Bléré, type_=, standard_value=Bléré, description=)>]

        :param db_session:
        :param query:
        :return:
        """
        nes_db = db_session.query(NamedEntitiesDB)\
            .filter_by(name=query)\
            .all()
        return nes_db

    @staticmethod
    def search_approximate(db_session: Session, query: str) -> List[NamedEntitiesDB]:
        """
        >>> db = DatabaseManager(False, False, os.path.join(DATABASE_DIRECTORY, TABLE_PUBLICATION_2004_FILENAME))
        >>> db.prepare()
        >>> SearchManager.search_approximate(Session(db.engine), "Bléré")
        [<NamedEntitiesDB(id=633, name=Bléré, type_=, standard_value=Bléré, description=)>, <NamedEntitiesDB(id=1807, name= Public. : "Bléré et son canton", B.1997, 350, type_=, standard_value= Public. : "Bléré et son canton", B.1997, 350, description=)>]

        :param db_session:
        :param query:
        :return:
        """
        nes_db = db_session.query(NamedEntitiesDB) \
            .filter(NamedEntitiesDB.name.ilike(f"%{query}%")) \
            .all()
        return nes_db  # [SearchResponse(text=ne_db.name, id_=ne_db.id_) for ne_db in nes_db]

    @staticmethod
    def get_published_work_pages_by_named_entity(db_session: Session, named_entity_id: int) \
            -> Union[None, List[PublishedWorkPagesDB]]:
        """
        >>> db = DatabaseManager(False, False, os.path.join(DATABASE_DIRECTORY, TABLE_PUBLICATION_2004_FILENAME))
        >>> db.prepare()
        >>> res = SearchManager.get_published_work_pages_by_named_entity(Session(db.engine), 633)
        >>> res[0]
        <PublishedWorkPagesDB(id_=815, published_work_id=11, text='Bléré - Bléré et son canion, voir Duchemin et Livernet - Cité, M. LXIV, 64 - Démogra- phie, voir Chassier. - Fontaine, M. LXIL 160 sq - Histoire, voir Commengçais, Luche - Monastère, B.1995, 415 - Monnaies, M', page_number=415, publication_entry_id=635>
        >>> res[1]
        <PublishedWorkPagesDB(id_=816, published_work_id=14, text='Bléré - Bléré et son canion, voir Duchemin et Livernet - Cité, M. LXIV, 64 - Démogra- phie, voir Chassier. - Fontaine, M. LXIL 160 sq - Histoire, voir Commengçais, Luche - Monastère, B.1995, 415 - Monnaies, M', page_number=64, publication_entry_id=635>

        :param db_session:
        :param named_entity_id:
        :return:
        """

        publication_entries_db = db_session.query(PublicationEntriesDB)\
            .filter_by(named_entity_id=named_entity_id)\
            .all()
        if publication_entries_db:
            responses = []
            for publication_entry_db in publication_entries_db:
                responses.extend(db_session.query(PublishedWorkPagesDB)\
                                 .filter_by(publication_entry_id=publication_entry_db.id_)\
                                 .all())
            return responses
        return None

    @staticmethod
    def get_published_work(db_session: Session, published_work_id: int) \
            -> Union[PublishedWorksDB, None]:
        """
        >>> db = DatabaseManager(False, False, os.path.join(DATABASE_DIRECTORY, TABLE_PUBLICATION_2004_FILENAME))
        >>> db.prepare()
        >>> SearchManager.get_published_work(Session(db.engine), 11)
        <PublishedWorksDB(id_=11, year=1995, publication_type=B.)>
        >>> SearchManager.get_published_work(Session(db.engine), 14)
        <PublishedWorksDB(id_=14, year=LXIV, publication_type=M.)>


        :param db_session:
        :param published_work_id:
        :return:
        """
        published_work_db = db_session.query(PublishedWorksDB)\
            .filter_by(id_=published_work_id)\
            .one_or_none()
        return published_work_db

    @staticmethod
    def get_data_from_query(db_session: Session, query: str):
        """
        >>> db = DatabaseManager(False, False, os.path.join(DATABASE_DIRECTORY, TABLE_PUBLICATION_2004_FILENAME))
        >>> db.prepare()
        >>> session = Session(db.engine)
        >>> SearchManager.get_data_from_query(session, "Bléré")
        {'query': 'Bléré', 'result': [{'named_entity': {'name': 'Bléré', 'type_': '', 'id_': 633, 'standard_value': 'Bléré', 'description': ''}, 'citation_published_work': {'text': 'Bléré - Bléré et son canion, voir Duchemin et Livernet - Cité, M. LXIV, 64 - Démogra- phie, voir Chassier. - Fontaine, M. LXIL 160 sq - Histoire, voir Commengçais, Luche - Monastère, B.1995, 415 - Monnaies, M', 'page_number': 415, 'id_': 815, 'published_work_id': 11, 'publication_entry_id': 635}, 'published_work': {'year': '1995', 'id_': 11, 'title': '', 'publication_type': 'B.'}}, {'named_entity': {'name': 'Bléré', 'type_': '', 'id_': 633, 'standard_value': 'Bléré', 'description': ''}, 'citation_published_work': {'text': 'Bléré - Bléré et son canion, voir Duchemin et Livernet - Cité, M. LXIV, 64 - Démogra- phie, voir Chassier. - Fontaine, M. LXIL 160 sq - Histoire, voir Commengçais, Luche - Monastère, B.1995, 415 - Monnaies, M', 'page_number': 64, 'id_': 816, 'published_work_id': 14, 'publication_entry_id': 635}, 'published_work': {'year': 'LXIV', 'id_': 14, 'title': '', 'publication_type': 'M.'}}]}

        :param db_session:
        :param query:
        :return:
        """
        responses = SearchManager.search(db_session, query)
        named_entities = []
        for response in responses:
            citations = SearchManager.get_published_work_pages_by_named_entity(db_session, response.id_)
            for citation in citations:
                if citation:
                    reference = SearchManager.get_published_work(db_session, citation.published_work_id)
                    if reference:
                        named_entities.append(dict(named_entity=NamedEntitiesData.from_db_to_data(response),
                                                   citation_published_work=PublishedWorkPagesData.from_db_to_data(citation),
                                                   published_work=PublishedWorksData.from_db_to_data(reference)))
        return dict(query=query, result=named_entities)



