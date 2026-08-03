
def fact(num):
    if num == 1:
        return 1

    return num * fact(num-1)

n = int(input('Enter the number :'))
result = fact(n)
print('Factotial of given no is :', result)  