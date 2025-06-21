import sys

def solve():
    s = sys.stdin.readline().strip()
    n = len(s)
    if n < 26:
        print(-1)
        return
    
    for i in range(n - 25):
        window = s[i:i+26]
        freq = {}
        missing_letters = []
        valid = True
        for c in window:
            if c != '?':
                if c in freq:
                    valid = False
                    break
                freq[c] = 1
        if not valid:
            continue
        
        # Collect missing letters
        missing_letters = []
        for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if c not in freq:
                missing_letters.append(c)
        
        # Check if number of ? matches missing letters
        if window.count('?') == len(missing_letters):
            # Replace ? in the window with missing letters
            new_window = []
            missing_ptr = 0
            for c in window:
                if c == '?':
                    new_window.append(missing_letters[missing_ptr])
                    missing_ptr += 1
                else:
                    new_window.append(c)
            # Construct the result
            result = list(s)
            result[i:i+26] = new_window
            # Replace remaining ? with 'A'
            for j in range(n):
                if result[j] == '?':
                    result[j] = 'A'
            print(''.join(result))
            return
    print(-1)

solve()