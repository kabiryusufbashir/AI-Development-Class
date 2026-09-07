from .similarity import cosine_similarity


def search_documents(query_vector, documents, document_vectors, top_k=3):
    results = []

    # Compare the query vector with every document vector.
    for index, document_vector in enumerate(document_vectors):
        similarity = cosine_similarity(query_vector, document_vector)

        # Store the document title and its similarity score together.
        results.append({
            "title": documents[index],
            "similarity": similarity
        })

    # Sort documents from most similar to least similar.
    sorted_results = sorted(
        results,
        key=lambda result: result["similarity"],
        reverse=True
    )

    # Return only the best matching documents.
    return sorted_results[:top_k]
