
def square(num):
    return num * num

def cube(num):
    return num * num * num

def operate(list, operation):
    for i in list:
        result = operation(i)
        print(result)

list = [5, 6, 7]
print('square result:')
result = operate(list, square)
print('cube result:')
result = operate(list, cube)
