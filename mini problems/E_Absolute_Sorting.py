import sys

def find_road_position(n, a):
    left_zeros = 0
    right_ones = a.count('1')  # Total ones in the array initially

    best_pos = 0
    min_dist = abs(n // 2 - best_pos)

    for i in range(n + 1):  # Considering the position after house i
        if i > 0 and a[i - 1] == '0':
            left_zeros += 1
        if i < n and a[i] == '1':
            right_ones -= 1

        if left_zeros >= (i + 1) // 2 and right_ones >= (n - i + 1) // 2:
            dist = abs(n // 2 - i)
            if dist < min_dist or (dist == min_dist and i < best_pos):
                best_pos = i
                min_dist = dist

    return best_pos

def solve():
    t = int(sys.stdin.readline().strip())
    results = [str(find_road_position(int(sys.stdin.readline().strip()), sys.stdin.readline().strip())) for _ in range(t)]
    sys.stdout.write("\n".join(results) + "\n")

solve()