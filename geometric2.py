def geom(p, n):
    q = 1 - p
    return q ** (n - 1) * p


def main():
    lRatio, rRatio = list(map(float, input().split()))
    p = lRatio / rRatio
    n = int(input())
    total = 5
    print(round(sum([geom(p, i) for i in range(1, total + 1)]), 3))


main()
