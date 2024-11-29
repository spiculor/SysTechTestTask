import spacy
import re


nlp = spacy.load("ru_core_news_sm")

def process_text(text: str):
    text = text.lower()
    text = re.sub(r"[^а-яА-ЯёЁ\s]", "", text)
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return tokens
