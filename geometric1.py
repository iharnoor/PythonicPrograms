lRatio, rRatio = list(map(float, input().split()))
p = lRatio / rRatio
n = int(input())
q = 1 - p
print(round((q ** (n - 1) * p), 3))
