#decorator will take function as argument
# And decorator will return same function 
# Function greater_first(fun) and logg_deco(fun1) are decorator 
def logg_deco(fun1):
    def wrap(a, b):
        print("Value :", a, " ", b)
        result = fun1(a, b)
        print("Result ", result)
        return result
    return wrap

def greater_first(fun): 
    def warp(a, b):
        if a<b:
            a,b = b,a
        return fun(a, b)    
    return warp

@logg_deco
@greater_first
def sub(a, b):
    # if a<b: # this code is replaced by decorator function
    #     a,b = b,a
    return a-b

@logg_deco
@greater_first    
def divide(a, b):
    # if a<b:# this code is replaced by decorator function
    #     a,b = b,a
    return a/b

result1 = divide(2, 4)
print(result1)
result2 = sub(2, 4)
print(result2)