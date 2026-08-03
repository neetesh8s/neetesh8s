
def fact(num):
    res = 1
    for i in range(1, num+1):
        res = res*i
    return res

n = int(input('Enter the number :'))
result = fact(n)
print('Factotial of given no is :', result)    