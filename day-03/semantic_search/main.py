from .data import documents, document_vectors, features, query, query_vector
from .search import search_documents


def main():
    top_results = search_documents(
        query_vector,
        documents,
        document_vectors,
        top_k=3
    )

    print("================================")
    print("        SEMANTIC SEARCH")
    print("================================")

    print("\nQuery:")
    print(query)

    print("\nFeature order:")
    print(features)

    print("\nExplanation:")
    print("Each document and the query are represented as vectors.")
    print("Similar meanings should have vectors pointing in similar directions.")
    print("Cosine similarity compares those directions and gives a score.")
    print("A higher score means the document is more similar to the query.")

    print("\nResults:")
    for position, result in enumerate(top_results, start=1):
        print(f"\n{position}. {result['title']}")
        print(f"   Similarity: {result['similarity']:.2f}")


if __name__ == "__main__":
    main()
