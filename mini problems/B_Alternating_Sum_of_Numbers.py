t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    seq = list(map(int, input().strip().split()))
    res = 0
    for idx in range(len(seq)):
        if idx % 2 == 0:
            res += seq[idx]
        else:
            res -= seq[idx]
    print(res)
