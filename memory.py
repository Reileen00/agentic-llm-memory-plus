from embeddings import embed
from vector_store import VectorStore
import time

stores={}

def get_store(user):
    if user not in stores:
        stores[user]=VectorStore()
    return stores[user]

def store_memory(user,text):
    e=embed([text])[0]
    get_store(user).add([e],[{"text":text,"time":time.time()}])

def retrieve(user,query):
    q=embed([query])[0]
    return get_store(user).search(q)
