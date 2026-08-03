#Simple addition function
def add():
    a = 4
    b = 5
    c = a + b
    print(c)

add()
#Below function is to pass the value at the time of runing and return addition
def add1(x,y):
    a = x
    b = y
    c = a+b
    return c

result = add1(5, 9)
print(f"The value of add1 is: {result}")
print(f"The value of add1 is: {add1(7, 9)}" )