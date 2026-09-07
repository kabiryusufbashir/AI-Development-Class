import numpy as np


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    # Cosine similarity measures how close two vectors point in the same direction.
    # The formula is:
    # dot product / (magnitude of a * magnitude of b)
    dot_product = np.dot(a, b)
    magnitude_a = np.linalg.norm(a)
    magnitude_b = np.linalg.norm(b)

    # If a vector has only zeros, its magnitude is 0.
    # Dividing by 0 would cause an error, so we return 0 similarity.
    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    similarity = dot_product / (magnitude_a * magnitude_b)
    return float(similarity)
