from memory import retrieve, store_memory
from decay import decay
import openai

openai.api_key="YOUR_KEY"

def agent(user,prompt):
    raw=retrieve(user,prompt)
    memories=decay(raw)

    context="\n".join(memories)
    final=f"Memory:\n{context}\nUser:{prompt}"

    r=openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":final}]
    )
    reply=r["choices"][0]["message"]["content"]

    store_memory(user,"User:"+prompt)
    store_memory(user,"Assistant:"+reply)
    return reply
