t = int(input())  
target = "01032025"  

for _ in range(t):
    n = int(input())  
    digits = list(map(int, input().split()))  
    
    target_count = {digit: target.count(str(digit)) for digit in range(10)}  
    current_count = {digit: 0 for digit in range(10)}  
    
    for i in range(n):
        current_digit = digits[i]
        if current_count[current_digit] < target_count[current_digit]:
            current_count[current_digit] += 1
        
        
        if all(current_count[digit] >= target_count[digit] for digit in range(10)):
            print(i + 1)  
            break
    else:
        print(0)  
