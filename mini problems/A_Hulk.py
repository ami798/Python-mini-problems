n = int(input())
feelings = []
for i in range(1, n + 1):
    if i % 2 != 0:
        feelings.append("I hate")
    else:
        feelings.append("I love")
result = " that ".join(feelings) + " it"
print(result)