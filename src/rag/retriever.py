def retrieve(store, query):
    result = store.search(query)
    if not result["chunks"]:
        raise ValueError("No chunks retrieved")
    return result
