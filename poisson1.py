from math import exp


def fact(n):
    return 1 if (n < 1) else n * fact(n - 1)


def poisson(k, lamb):
    return lamb ** k * exp(-lamb) / fact(k)


def main():
    lamb = float(input())
    k = float(input())
    print(round(poisson(k, lamb), 3))


main()
