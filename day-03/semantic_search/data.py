import numpy as np


# These are the document titles our small search engine can return.
documents = [
    "Fraud Detection with Machine Learning",
    "Artificial Intelligence in Banking",
    "Transaction Risk Analysis",
    "Cooking Recipes for Beginners",
    "Football Match Predictions"
]


# These feature names explain what each number in a vector means.
# For example, the first number represents how much the document relates to AI.
features = [
    "ai",
    "banking",
    "fraud",
    "risk",
    "food",
    "sports"
]


# Each document is represented as a vector of numbers.
# The vector values are manual scores between 0 and 1.
# Higher values mean the document is more related to that feature.
document_vectors = np.array([
    [0.95, 0.50, 0.98, 0.80, 0.00, 0.00],
    [0.90, 0.95, 0.55, 0.35, 0.00, 0.00],
    [0.35, 0.80, 0.65, 0.95, 0.00, 0.00],
    [0.00, 0.00, 0.00, 0.00, 0.98, 0.00],
    [0.20, 0.00, 0.00, 0.10, 0.00, 0.95]
])


# This query vector represents: "AI systems for detecting fraud".
# It has the same 6 features as the document vectors.
query = "AI systems for detecting fraud"
query_vector = np.array([1.00, 0.40, 1.00, 0.70, 0.00, 0.00])
