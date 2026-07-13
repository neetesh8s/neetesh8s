from array import *

#array keyword is to conver list in array
# 'i' what type of data we need to store in array

arr1 = array('i', [20, 30, 40, 55])
# insert value in array in last 
arr1.append(66)

# Reverse the arrary
arr1.reverse()

print("Array value are :")
for n in arr1:
    print(n)

#coppy the arrary value into another array
arr2 = array('i', arr1.tolist()) 
print(f'Array 2 is : {arr2}')

# to get the parrent array type use below code 
arr3 =array(arr1.typecode, arr1.tolist())
print(f'Array 3 is : {arr3}')

# other way of coppy without using tolist() fun
arr4 =array(arr1.typecode, (n for n in arr1))
print(f'Array 4 is : {arr4}')

# after coppy insert value in array 1
arr1[1] = 54
print(f'Array 1 is : {arr1}')