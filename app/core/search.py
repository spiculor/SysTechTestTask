from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


with open("data.txt", "r", encoding="utf-8") as file:
    documents = [line.strip() for line in file.readlines()]


vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

def search(query: str, top_n: int = 3):
    if not query.strip():
        return []
    query_vector = vectorizer.transform([query])
    similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    if similarities.max() == 0:
        return []
    top_indices = similarities.argsort()[-top_n:][::-1]
    results = [documents[i] for i in top_indices]
    return results