def solve():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, k = map(int, input[ptr:ptr + 2])
        ptr += 2
        b = list(map(int, input[ptr:ptr + n]))
        ptr += n
        
        product_b = 1
        for num in b:
            product_b *= num
        
        if 2023 % product_b != 0:
            print("NO")
            continue
        
        remaining_product = 2023 // product_b
        # Now, we need to split remaining_product into k integers >=1
        # We can try to factorize remaining_product into k factors
        # For k=1, it's trivial
        if k == 1:
            print("YES")
            print(remaining_product)
            continue
        
        # For k>1, we need to find k integers >=1 that multiply to remaining_product
        # Let's try to split into 1s and remaining_product
        # For example, if remaining_product is 7 and k=2, we can have [7,1]
        factors = []
        temp = remaining_product
        # We'll try to split into as many 1s as possible, and the rest into temp
        if temp == 1:
            if k >= 1:
                factors = [1] * k
            else:
                print("NO")
                continue
        else:
            if k == 0:
                if temp == 1:
                    print("YES")
                    print()
                else:
                    print("NO")
                continue
            # We can have k-1 ones and temp
            if (k - 1) >= 0:
                factors = [1] * (k - 1)
                factors.append(temp)
            else:
                print("NO")
                continue
        
        # Verify the product of factors is remaining_product and len(factors) == k
        product = 1
        for num in factors:
            product *= num
        if product == remaining_product and len(factors) == k:
            print("YES")
            print(' '.join(map(str, factors)))
        else:
            print("NO")

solve()