from array import *

#array keyword is to conver list in array
# 'i' what type of data we need to store in array

arr1 = array('i', [20, 30, 40, 55])
print(type(arr1))
#print array

print(arr1) # O/P-array('i', [20, 30, 40, 55])

# to print only array value conver array to list and print

print(arr1.tolist()) #O/P-[20, 30, 40, 55]

# Print value one by one
print("Array value are :")
for n in arr1:
    print(n)


