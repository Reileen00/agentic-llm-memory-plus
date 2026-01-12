from agent import agent

print("With memory:")
agent("u","I like finance")
print(agent("u","What should I read?"))

print("\nWithout memory:")
print(agent("new","What should I read?"))
