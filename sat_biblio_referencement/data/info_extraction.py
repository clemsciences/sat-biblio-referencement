
import re

from sat_biblio_referencement.data.abbreviations import Abbreviations


class Extractor:

    @staticmethod
    def extract_citation(text: str):
        """
        >>> Extractor.extract_citation("Abilly - Archéolab, B.2002, 9 - Forges, B.1996, 669 ; sidérurgie, voir Guichard - Habitat, voir Rousseau - Néolithique, voir Marquet - Tessons protohistoriques, voir Geslin et Schoenstein - Lieux-dits : Le Fouion, fouilles 1994 : voir Millet-Richard ; B.2000, 382 - Le Petit- Paulmy, B.1997, 344 ; B.2000, 382 - Site de la Grosse Coue, voir Millet-Richard")
        [{'work': 'B.', 'year': '2002', 'page': '9'}, {'work': 'B.', 'year': '1996', 'page': '669'}, {'work': 'B.', 'year': '2000', 'page': '382'}, {'work': 'B.', 'year': '1997', 'page': '344'}, {'work': 'B.', 'year': '2000', 'page': '382'}]

        :param text:
        :return:
        """
        l = []

        bulletin_pattern = re.compile(r"B\.( )?(?P<year>[0-9]+), (?P<page>[0-9]+)( sq\.)?")
        m = bulletin_pattern.search(text)
        while m:
            l.append(dict(work=Abbreviations.B, year=m.group("year"), page=m.group("page")))
            beginning_i = m.end() + 1
            m = bulletin_pattern.search(text, pos=beginning_i)

        memoire_pattern = re.compile(r"M\.( )?(?P<number>[IVXLCDM]+), (?P<page>[0-9]+)(sq\.)?")
        m = memoire_pattern.search(text)
        while m:
            l.append(dict(work=Abbreviations.M, number=m.group("number"), page=m.group("page")))
            beginning_i = m.end() + 1
            m = memoire_pattern.search(text, pos=beginning_i)
        return l

    @staticmethod
    def extract_named_entity(text: str):
        """
        >>> Extractor.extract_named_entity("Abilly - Archéolab, B.2002, 9 - Forges, B.1996, 669 ; sidérurgie, voir Guichard - Habitat, voir Rousseau - Néolithique, voir Marquet - Tessons protohistoriques, voir Geslin et Schoenstein - Lieux-dits : Le Fouion, fouilles 1994 : voir Millet-Richard ; B.2000, 382 - Le Petit- Paulmy, B.1997, 344 ; B.2000, 382 - Site de la Grosse Coue, voir Millet-Richard")
        'Abilly'

        :param text:
        :return:
        """
        named_entity = text.split(" - ")[0]

        return named_entity

    @staticmethod
    def see_this(text: str):
        l = []
        bulletin_pattern = re.compile(r"voir( aussi)? (?P<named_entity>[ \w]+)")
        m = bulletin_pattern.search(text)
        while m:
            l.append(dict(named_entity=m.group("named_entity")))
            beginning_i = m.end() + 1
            m = bulletin_pattern.search(text, pos=beginning_i)
