import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class SemanticSearch:

    def __init__(self):

        self.vectorizer = TfidfVectorizer()
        self.files = []
        self.matrix = None

    def index_files(self, files):

        texts = []

        for f in files:

            name = os.path.basename(f)
            text = name.replace("_", " ").replace("-", " ")

            texts.append(text)

        if not texts:
            return

        self.files = files
        self.matrix = self.vectorizer.fit_transform(texts)

    def search(self, query):

        if self.matrix is None:
            return []

        q = self.vectorizer.transform([query])

        sims = cosine_similarity(q, self.matrix).flatten()

        ranked = sorted(
            zip(self.files, sims),
            key=lambda x: x[1],
            reverse=True
        )

        return [r[0] for r in ranked if r[1] > 0.1]