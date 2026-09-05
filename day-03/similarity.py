import numpy as np

def cosine_similarity(a:np.ndarray, b:np.ndarray) -> float:
    dot_product = np.dot(a, b)

    magnitude_a = np.linalg.norm(a)
    magnitude_b = np.linalg.norm(b)

    similarity = dot_product / (magnitude_a * magnitude_b)

    return float(similarity)

vector_a = np.array([1, 2, 3])
vector_b = np.array([20, 14, 36])

score = cosine_similarity(vector_a, vector_b)
print("Cosine Similarity:", score)