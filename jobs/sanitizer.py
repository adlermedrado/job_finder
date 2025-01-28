import spacy
import unicodedata
import re


class MultiLangSanitizer:
    def __init__(self):
        self.en_nlp = spacy.load('en_core_web_sm')
        self.pt_nlp = spacy.load('pt_core_news_sm')

    def sanitize(self, text: str) -> str:
        en_doc = self.en_nlp(text)
        text = self._remove_entities(en_doc)

        pt_doc = self.pt_nlp(text)
        text = self._remove_entities(pt_doc)

        text = self._clean_text(text)

        return text

    def _remove_entities(self, doc):
        return ' '.join(
            token.text for token in doc if token.ent_type_ not in {'PERSON', 'ORG', 'EMAIL', 'GPE', 'PHONE'}
        )

    def _clean_text(self, text: str) -> str:
        text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
        text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', '', text)
        text = re.sub(r'\b\d{1,3}[-.\s]??\d{1,4}[-.\s]??\d{1,4}\b', '', text)
        text = re.sub(r'\b\(\d{1,3}\)\s*\d{1,4}[-.\s]??\d{1,4}\b', '', text)
        text = re.sub(r'[^A-Za-z0-9\s]', '', text)
        text = re.sub(r'\s+', ' ', text)

        return text.strip()
