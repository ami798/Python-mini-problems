n = int(input())
t = list(map(int, input().split()))

alice = 0
bob = n - 1
time_alice = 0
time_bob = 0

count_alice = 0
count_bob = 0

while alice <= bob:
    if time_alice <= time_bob:
        time_alice += t[alice]
        count_alice += 1
        alice += 1
    else:
        time_bob += t[bob]
        count_bob += 1
        bob -= 1

print(count_alice, count_bob)
