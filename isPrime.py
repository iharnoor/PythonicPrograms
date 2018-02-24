def isPrime(num):
    if num < 2:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        for i in range(3, int(num ** .5 + 1)):
            if num % i == 0:
                return False
    return True


p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    printVal = 'Not prime' if isPrime(n) == False else 'Prime'
    print(printVal)
