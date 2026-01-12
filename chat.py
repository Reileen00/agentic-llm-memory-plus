from agent import agent

user="baisnabi"
print("Type exit to quit")

while True:
    q=input("> ")
    if q=="exit":
        break
    print(agent(user,q))
