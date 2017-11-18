def getMean(N, nums):
    return sum(nums) / N


def getDeviation(N, nums):
    mean = getMean(N, nums)
    error = [(x - mean) ** 2 for x in nums]
    variance = getMean(N, error)
    stdDeviation = variance ** 0.5
    return stdDeviation


N = int(input())
nums = sorted([int(num) for num in input().split()])
dev = getDeviation(N, nums)
print(round(dev, 1))
