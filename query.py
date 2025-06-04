from embedder import get_embedding

def search_resumes(store, job_desc):
    query_vector = get_embedding(job_desc)
    return store.search(query_vector)
