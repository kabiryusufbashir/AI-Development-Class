import numpy as np


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    # Cosine similarity formula:
    # similarity = dot product of a and b / (length of a * length of b)
    dot_product = np.dot(a, b)
    magnitude_a = np.linalg.norm(a)
    magnitude_b = np.linalg.norm(b)

    similarity = dot_product / (magnitude_a * magnitude_b)
    return float(similarity)


# Each row represents one document vector.
# Each number can represent how strongly a document relates to a feature/topic.
document_vectors = np.array([
    [0.9, 0.1, 0.2, 0.7],
    [0.2, 0.8, 0.6, 0.1],
    [0.8, 0.2, 0.1, 0.9],
    [0.1, 0.9, 0.7, 0.2],
    [0.7, 0.3, 0.4, 0.8]
])

# This is the user's search/query vector.
# It must have the same number of features as each document vector.
query_vector = np.array([1.0, 0.2, 0.3, 0.8])

similarity_scores = []

for index, document_vector in enumerate(document_vectors):
    score = cosine_similarity(query_vector, document_vector)
    similarity_scores.append((index + 1, score))

# Sort from highest similarity to lowest similarity.
sorted_scores = sorted(similarity_scores, key=lambda item: item[1], reverse=True)

top_3_documents = sorted_scores[:3]

print("Query vector:", query_vector)
print("Document vectors:")
print(document_vectors)

print("Similarity scores:")
for document_number, score in similarity_scores:
    print("Document", document_number, "similarity:", score)

print("Top 3 most similar documents:")
for document_number, score in top_3_documents:
    print("Document", document_number, "similarity:", score)
