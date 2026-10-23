import os
import faiss
from sentence_transformers import SentenceTransformer


# =========================================================
# 1. KNOWLEDGE FOLDER
# =========================================================

KNOWLEDGE_FOLDER = "knowledge"


# =========================================================
# 2. LOAD KNOWLEDGE FILES
# =========================================================

def load_documents():

    documents = []

    for filename in os.listdir(KNOWLEDGE_FOLDER):

        if filename.endswith(".txt"):

            file_path = os.path.join(
                KNOWLEDGE_FOLDER,
                filename
            )

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                text = file.read()

            documents.append({
                "filename": filename,
                "text": text
            })

    return documents


# =========================================================
# 3. CREATE TEXT CHUNKS
# =========================================================

def create_chunks(text, chunk_size=500):

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunk = text[i:i + chunk_size]

        chunks.append(chunk)

    return chunks


# =========================================================
# 4. BUILD KNOWLEDGE BASE
# =========================================================

def build_knowledge_base():

    documents = load_documents()

    all_chunks = []

    for document in documents:

        chunks = create_chunks(document["text"])

        for chunk in chunks:

            all_chunks.append({
                "text": chunk,
                "source": document["filename"]
            })

    print("Total chunks:", len(all_chunks))

    return all_chunks


# =========================================================
# 5. CREATE EMBEDDINGS
# =========================================================

def create_embeddings(chunks):

    print("Loading embedding model...")

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    embeddings = model.encode(
        texts,
        convert_to_numpy=True
    )

    print("Embeddings created:", embeddings.shape)

    return model, embeddings


# =========================================================
# 6. CREATE FAISS VECTOR DATABASE
# =========================================================

def create_faiss_index(embeddings):

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    faiss.write_index(
        index,
        "rag/travel_index.faiss"
    )

    print("FAISS index created and saved!")

    return index

# =========================================================
# 7. SEARCH KNOWLEDGE BASE
# =========================================================

def search_knowledge(
    query,
    model,
    index,
    chunks,
    top_k=3
):

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    )

    distances, results = index.search(
        query_embedding,
        top_k
    )

    retrieved_chunks = []

    for result in results[0]:

        retrieved_chunks.append(
            chunks[result]
        )

    return retrieved_chunks

def get_relevant_information(query, top_k=3):

    chunks = build_knowledge_base()

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    index = faiss.read_index(
        "rag/travel_index.faiss"
    )

    results = search_knowledge(
        query,
        model,
        index,
        chunks,
        top_k
    )

    return results    


# =========================================================
# 8. TEST RAG
# =========================================================

if __name__ == "__main__":

    chunks = build_knowledge_base()

    model, embeddings = create_embeddings(chunks)

    index = create_faiss_index(embeddings)

    query = "I want a beach trip"

    results = search_knowledge(
        query,
        model,
        index,
        chunks
    )

    print("\nUSER QUERY:")
    print(query)

    print("\nRELEVANT INFORMATION:\n")

    for result in results:

        print("SOURCE:", result["source"])
        print(result["text"])
        print("-" * 60)