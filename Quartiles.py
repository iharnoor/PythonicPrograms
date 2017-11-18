def median(nums):
    return sum(nums[len(nums) // 2 - 1:len(nums) // 2 + 1]) // 2 if len(nums) % 2 == 0 else nums[len(nums) // 2]


def quartiles(N, nums):
    Q1 = median(nums[:len(nums) // 2])
    Q2 = median(nums)
    Q3 = median(nums[len(nums) // 2:]) if N % 2 == 0 else median(nums[len(nums) // 2 + 1:])
    return Q1, Q2, Q3


N = int(input())
nums = sorted([int(num) for num in input().split()])
Q1, Q2, Q3 = quartiles(N, nums)
print(Q1)
print(Q2)
print(Q3)
