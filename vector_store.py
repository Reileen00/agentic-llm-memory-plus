import numpy as np

class VectorStore:
    def __init__(self):
        self.vectors=[]
        self.payloads=[]

    def add(self,embeddings,payloads):
        for e,p in zip(embeddings,payloads):
            self.vectors.append(e)
            self.payloads.append(p)

    def search(self,query,k=5):
        sims=np.dot(self.vectors,query)
        idx=np.argsort(sims)[-k:][::-1]
        return [self.payloads[i] for i in idx]
