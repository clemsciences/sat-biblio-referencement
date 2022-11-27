from sat_biblio_referencement.database.published_work_table import PublishedWorksDB, PublishedWorkPagesDB, \
    PublishedWorkArticlesDB


class PublishedWorksData:

    @staticmethod
    def from_data_to_db(published_work: dict) -> PublishedWorksDB:
        published_work_db = PublishedWorksDB()
        published_work_db.year = published_work.get("year", "")
        published_work_db.id_ = published_work.get("id_", None)
        published_work_db.title = published_work.get("title", "")
        published_work_db.publication_type = published_work.get("publication_type", "")
        return published_work_db

    @staticmethod
    def from_db_to_data(published_work_db: PublishedWorksDB):
        return dict(
            year=published_work_db.year,
            id_=published_work_db.id_,
            title=published_work_db.title,
            publication_type=published_work_db.publication_type
        )


class PublishedWorkPagesData:

    @staticmethod
    def from_data_to_db(published_work_page: dict) -> PublishedWorkPagesDB:
        published_work_page_db = PublishedWorkPagesDB()
        published_work_page_db.text = published_work_page.get("text", "")
        published_work_page_db.page_number = published_work_page.get("page_number", None)
        published_work_page_db.id_ = published_work_page.get("id_", None)
        published_work_page_db.published_work_id = published_work_page.get("published_work_id", None)
        published_work_page_db.publication_entry_id = published_work_page.get("publication_entry_id", None)
        return published_work_page_db

    @staticmethod
    def from_db_to_data(published_word_page_db: PublishedWorkPagesDB) -> dict:
        return dict(
            text=published_word_page_db.text,
            page_number=published_word_page_db.page_number,
            id_=published_word_page_db.id_,
            published_work_id=published_word_page_db.published_work_id,
            publication_entry_id=published_word_page_db.publication_entry_id
        )


class PublishedWorkArticlesData:

    @staticmethod
    def from_data_to_db(published_work_article: dict) -> PublishedWorkArticlesDB:
        published_work_page_db = PublishedWorkArticlesDB()
        published_work_page_db.title = published_work_article.get("title", "")
        published_work_page_db.page_number_start = published_work_article.get("page_number_start", None)
        published_work_page_db.page_number_end = published_work_article.get("page_number_end", None)
        published_work_page_db.id_ = published_work_article.get("id_", None)
        published_work_page_db.published_work_id = published_work_article.get("published_work_id", None)
        return published_work_page_db

    @staticmethod
    def from_db_to_data(published_word_article_db: PublishedWorkArticlesDB) -> dict:
        return dict(
            title=published_word_article_db.title,
            page_number_start=published_word_article_db.page_number_start,
            page_number_end=published_word_article_db.page_number_end,
            id_=published_word_article_db.id_,
            published_work_id=published_word_article_db.published_work_id,
        )

