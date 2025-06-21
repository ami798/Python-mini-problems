n = int(input())
laptops = []
for _ in range(n):
    a, b = map(int, input().split())
    laptops.append((a, b))


laptops.sort()


happy = False
for i in range(n - 1):
    if laptops[i][1] > laptops[i + 1][1]:
        happy = True
        break

print("Happy Alex" if happy else "Poor Alex")