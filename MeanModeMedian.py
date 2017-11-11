import numpy as numPy
from scipy import stats
from collections import Counter

size = int(input())  # Get the size of the list
numbers = list(map(int, input().split()))  # store the next line of numbers in the list
print('Mean=',numPy.mean(numbers))
print('Median=',numPy.median(numbers))
print('Mode=',int(stats.mode(numbers)[0]))

# Second way of doing
print('Second Way: ')

data = sorted(numbers)

Mean = sum(data) / size
Median = (data[size // 2] + data[-(size // 2 + 1)]) / 2
Mode = sorted(sorted(Counter(data).items()), key=lambda x: x[1], reverse=True)[0][0]

print(Mean, Median, Mode, sep='\n')
