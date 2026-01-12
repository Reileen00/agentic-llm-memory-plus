import time

def decay(memories,half_life=3600):
    now=time.time()
    weighted=[]
    for m in memories:
        age=now-m["time"]
        w=0.5**(age/half_life)
        weighted.append((w,m["text"]))
    weighted.sort(reverse=True)
    return [m for _,m in weighted[:5]]
