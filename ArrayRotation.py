def array_left_rotation(a, n, k):
    for x in range(k):
        a.append(0)
        swap(a, 0, len(a) - 1)
        a.pop(0)
    return a

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
    

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')