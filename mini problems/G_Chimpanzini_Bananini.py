import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    results = []
    for _ in range(t):
        q = int(input[ptr])
        ptr += 1
        array = []
        rizziness = 0
        length = 0
        reversed_flag = False
        for __ in range(q):
            s = int(input[ptr])
            ptr += 1
            if s == 1:
                # Cyclic shift
                if length == 0:
                    pass
                else:
                    if reversed_flag:
                        # The array is reversed, so cyclic shift is equivalent to moving the first element to the end
                        first_element = array.pop(0)
                        array.append(first_element)
                        # Update rizziness
                        rizziness -= first_element * 1
                        rizziness += first_element * length
                    else:
                        # The array is not reversed, so cyclic shift is moving the last element to the front
                        last_element = array.pop()
                        array.insert(0, last_element)
                        # Update rizziness
                        rizziness -= last_element * length
                        rizziness += last_element * 1
                        # Adjust the rest of the elements
                        rizziness += sum(array[1:])  # Each element's index increases by 1
            elif s == 2:
               
                reversed_flag = not reversed_flag
     
                rizziness = 0
                for i in range(length):
                    if reversed_flag:
                        rizziness += array[length - 1 - i] * (i + 1)
                    else:
                        rizziness += array[i] * (i + 1)
            elif s == 3:
                k = int(input[ptr])
                ptr += 1
                if reversed_flag:
                    array.insert(0, k)
                else:
                    array.append(k)
                length += 1
                rizziness += k * length
            results.append(str(rizziness))
        results.append('\n')
    print('\n'.join(results))

solve()