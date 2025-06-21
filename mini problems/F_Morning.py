t = int(input())
for _ in range(t):
    pin = input().strip()
    current = '1'
    total_time = 0
    for digit in pin:
        if current == digit:
            total_time += 1
        else:
            
            current_pos = int(current)
            target_pos = int(digit)
            
            
            if current == '0':
                current_pos = 10
            if digit == '0':
                target_pos = 10
            total_time += abs(current_pos - target_pos) + 1  
            current = digit
    print(total_time)