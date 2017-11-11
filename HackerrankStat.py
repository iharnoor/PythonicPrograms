import collections

N = int(input())
numbers = sorted(int(val) for val in input().split())
counts = collections.Counter(numbers)

# Find total and mean
totals = (val * count for val, count in counts.items())
mean = sum(totals) / N

# Find median
middle, is_odd_length = divmod(N, 2)
if is_odd_length:
    median = numbers[middle]
    
else:
    median = (numbers[middle - 1] + numbers[middle]) / 2
    
# Find mode
freq = 0
mode = 0
for val, count in counts.items():
    if count > freq:
        mode = val
        freq = count
        
    elif count == freq and val < mode:
        mode = val

print(mean)
print(median)
print(mode)