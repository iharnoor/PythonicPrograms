n = int(input())
nums = [int(x) for x in input().split()]
weight = [int(x) for x in input().split()]
print(round(1.0*sum([nums[i]*weight[i] for i in range(n)])/sum(weight), 1))