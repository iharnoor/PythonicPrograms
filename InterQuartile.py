def median(nums):
    return sum(nums[len(nums) // 2 - 1:len(nums) // 2 + 1]) // 2 if len(nums) % 2 == 0 else nums[len(nums) // 2]


def quartiles(N, nums):
    Q1 = median(nums[:len(nums) // 2])
    Q2 = median(nums)
    Q3 = median(nums[len(nums) // 2:]) if N % 2 == 0 else median(nums[len(nums) // 2 + 1:])
    return Q1, Q2, Q3


N = int(input())
nums = list(map(int, input().split()))
freq = list(map(int, input().split()))
newList = []
for i in range(N):
    newList += [nums[i]] * freq[i]
newList.sort()
Q1, Q2, Q3 = quartiles(N, newList)
print(round(float(Q3 - Q1), 1))
