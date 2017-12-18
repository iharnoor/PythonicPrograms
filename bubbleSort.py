def bubbleSort(a, n):
    numberOfSwaps = 0
    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                swap(a, j, j + 1)
                numberOfSwaps += 1
        if numberOfSwaps == 0:
            break
    return a, numberOfSwaps


def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


def Main():
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    a, numSwaps = bubbleSort(a, n)
    print('Array is sorted in', numSwaps, 'swaps.')
    print('First Element:', a[0])
    print('Last Element:', a[n - 1])


Main()
