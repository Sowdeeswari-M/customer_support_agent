from rag.retriever import retrieve_documents

query = "How do I reset my router?"

results = retrieve_documents(query)

print("=" * 50)

for i, doc in enumerate(results, 1):
    print(f"\nDocument {i}\n")
    print(doc.page_content)