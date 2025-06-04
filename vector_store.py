from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class ResumeVectorStore:
    def __init__(self):
        self.embeddings = []
        self.metadata = []

    def add(self, vector, meta):
        self.embeddings.append(vector)
        self.metadata.append(meta)

    def build_index(self):
        self.embedding_matrix = np.array(self.embeddings)

    def search(self, query_vector, k=3):
        query_vector = np.array(query_vector).reshape(1, -1)
        similarities = cosine_similarity(query_vector, self.embedding_matrix)[0]
        top_k_indices = similarities.argsort()[-k:][::-1]

        results = []
        for i in top_k_indices:
            score = similarities[i]
            results.append((self.metadata[i], float(score)))
        return results
