from sat_biblio_referencement.database.named_entities_table import NamedEntitiesDB
from sat_biblio_referencement.database.publication_entries_table import PublicationEntriesDB


class PublicationEntriesData:

    @staticmethod
    def from_db_to_data(publication_table_db: PublicationEntriesDB):
        return dict(
            text=publication_table_db.text,
            named_entity_id=publication_table_db.named_entity_id,
            id_=publication_table_db.id_
        )

    @staticmethod
    def from_data_to_db(publication_table: dict) -> PublicationEntriesDB:
        publication_entry_db = PublicationEntriesDB()
        publication_entry_db.text = publication_table.get("text", "")
        publication_entry_db.named_entity_id = publication_table.get("named_entity_id", None)
        publication_entry_db.id_ = publication_table.get("id_", None)
        return publication_entry_db


class NamedEntitiesData:
    @staticmethod
    def from_db_to_data(named_entity_db: NamedEntitiesDB):
        return dict(
            name=named_entity_db.name,
            type_=named_entity_db.type_,
            id_=named_entity_db.id_,
            standard_value=named_entity_db.standard_value,
            description=named_entity_db.description
        )

    @staticmethod
    def from_data_to_db(named_entity: dict) -> NamedEntitiesDB:
        publication_entry_db = NamedEntitiesDB()
        publication_entry_db.name = named_entity.get("name", "")
        publication_entry_db.type_ = named_entity.get("type_", "")
        publication_entry_db.description = named_entity.get("description", None)
        publication_entry_db.standard_value = named_entity.get("standard_value", None)
        publication_entry_db.id_ = named_entity.get("id_", None)
        return publication_entry_db


