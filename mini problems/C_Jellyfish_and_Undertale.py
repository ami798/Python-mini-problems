t = int(input().strip())
results = []

for _ in range(t):
    a, b, n = map(int, input().strip().split())
    tools = list(map(int, input().strip().split()))
    
    tools.sort(reverse=True)  # Prioritize tools with the largest value
    timer = b
    time_elapsed = 0
    
    # Use tools optimally
    for tool in tools:
        if timer == 0:
            break
        # Use the tool to maximize the timer
        if timer < a:
            timer = min(timer + tool, a)
        time_elapsed += 1  # 1 second passes for tool usage
        timer -= 1  # Timer decreases naturally after 1 second
    
    # Add remaining time until the timer reaches 0
    if timer > 0:
        time_elapsed += timer  # Add natural countdown
    
    results.append(time_elapsed)

print("\n".join(map(str, results)))
