def max_binary_after_deletion(a: str) -> str:
    for i in range(len(a)):
        if a[i] == '0':
            return a[:i] + a[i+1:]  # remove the first 0
    return a[:-1]  # no 0 found → remove last digit
