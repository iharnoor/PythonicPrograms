"""
 Problem: To add one to the last element of the array just like addition of whole numbers
 for example: [1,3,4,5] +1 changes to [1,3,4,6]
"""


# Case 1: [1,3,4]->[1,3,4]
# Case 2: [1,9,9]->[2,0,0]
# Case 3: [9,9,9]->[1,0,0,0]

# Assumptions: that any element in an array ranges from 0 to 9

def addArray(array):
    carry = 1
    sum = 0
    for i in range(len(array) - 1, -1, -1):
        sum = array[i] + carry
        if sum == 10:
            carry = 1
        else:
            carry = 0
        array[i] = sum % 10
    if carry == 1:
        newArray = array
        newArray.append(0)
        newArray[0] = carry
        array = newArray
    return array


print('Array1: ', addArray([1, 9, 9, 9]))
print('Array2: ', addArray([9, 9, 9, 9]))
print('Array3: ', addArray([1, 3, 4]))
