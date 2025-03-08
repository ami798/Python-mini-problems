def the_num(a, b):
    if a == 0:
        print(1)
    else:
        print(a + 2 * b + 1)

n = int(input().strip())
for _ in range(n):
    a, b = map(int, input().strip().split())
    the_num(a, b)
