
def outer():
    print('Outer function')

    def inner():
        print('Inner function')

    #inner()    
    return inner
something = outer()
print(something)
something()