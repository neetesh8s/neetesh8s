
class Duck:

    def fly(self):
        return "Duck flying"

    def swim(self):
        return "Duck swiming"

class Airplane:

    def fly(self):
        return "Airplane Flying"

def fly_test(object):
    print(object.fly())

# Create objects

duck = Duck()
airplane = Airplane()
print(duck.swim())
# Same function works with different objects
fly_test(duck)        # Output: Duck flying
fly_test(airplane)    # Output: Airplane flying

