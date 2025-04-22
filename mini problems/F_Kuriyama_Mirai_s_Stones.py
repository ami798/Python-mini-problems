import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    v = list(map(int, input[ptr:ptr + n]))
    ptr += n
    
    
    prefix_original = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_original[i] = prefix_original[i - 1] + v[i - 1]
    
    
    sorted_v = sorted(v)
    prefix_sorted = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sorted[i] = prefix_sorted[i - 1] + sorted_v[i - 1]
    
    m = int(input[ptr])
    ptr += 1
    output = []
    for _ in range(m):
        type_q = int(input[ptr])
        l = int(input[ptr + 1])
        r = int(input[ptr + 2])
        ptr += 3
        if type_q == 1:
            sum_q = prefix_original[r] - prefix_original[l - 1]
        else:
            sum_q = prefix_sorted[r] - prefix_sorted[l - 1]
        output.append(str(sum_q))
    
    print('\n'.join(output))

if __name__ == '__main__':
    main()