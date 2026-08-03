from functools import reduce
arr = [2, 4, 6, 5, 11, 10, 8, 7, 9]
# even = []
# odd = []
# for i in arr:
#     if i % 2 ==0:
#         even.append(i)
#     else:
#         odd.append(i)

# print(even)
# print(odd)

# use inbuild filter() method to calculate even and odd

# def is_even(n): # we can use lambda for this

#     return n % 2 ==0

# is_even = lambda n: n % 2 ==0
# evens = list(filter(is_even, arr)) # filter will return object and nned to convert in list
evens = list(filter(lambda n: n % 2 == 0, arr)) #replace evens = list(filter(is_even, arr))

double = list(map(lambda d: d * 2, evens)) # double evens list

# def sum_it(a, b):
#     return a+b
# sum = reduce(sum_it, double)

sum = reduce(lambda a,b: a+b, double)

print('using filter method :')
print('Even :', evens)
print('Double :', double)
print('Total :', sum)