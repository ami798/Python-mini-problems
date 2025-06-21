t = int(input())
for _ in range(t):
    s = input().strip()
    changed = True
    while changed and len(s) > 1:
        changed = False
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                # Perform the operation: replace s[i] with any letter (choice doesn't matter for adjacent)
                # Here, replacing with 'a' for simplicity
                new_char = 'a'
                s = s[:i] + new_char + s[i+2:]
                changed = True
                break  # Restart scanning after modification
    print(len(s))