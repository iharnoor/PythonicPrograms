def recursiveGCD(x, y):
    return x if y == 0 else recursiveGCD(y, x % y)


def GCD(x, y):
    while y != 0:
        rem = x % y
        x = y
        y = rem
    return x


def LCM(a, b):
    lcm = a if a > b else b

    while True:
        if lcm % a == 0 and lcm % b == 0:
            return lcm
        lcm += 1


a, b = input().strip().split(' ')
a, b = [int(a), int(b)]

print("Recursive GCD =", recursiveGCD(a, b))
print("Simple GCD =", GCD(a, b))

print("Simple LCM =", LCM(a, b))
print("Simple LCM using GCD=", a * b / GCD(a, b))
