def fact(n):
    return 1 if n == 0 else n * fact(n - 1)


def comb(n, r):
    return fact(n) / (fact(r) * fact(n - r))


def b(n, r, p):
    return comb(n, r) * (p ** r) * ((1 - p) ** (n - r))


prob, num = input().strip().split(' ')
prob = int(prob)
num = int(num)
prob /= 100

limit = 2
most2 = (round(sum([b(num, i, prob) for i in range(limit + 1)]), 3))
min2 = (round(sum([b(num, i, prob) for i in range(limit, num)]), 3))

print(most2)
print(min2)
