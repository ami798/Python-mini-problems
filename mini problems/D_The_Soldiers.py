
n = int(input())
coolness_factors = list(map(int, input().split()))

coolness_factors.sort()

coins_spent = 0


for i in range(1, n):
    if coolness_factors[i] <= coolness_factors[i - 1]:
        
        increment = coolness_factors[i - 1] - coolness_factors[i] + 1
        coolness_factors[i] += increment
        coins_spent += increment


print(coins_spent)
