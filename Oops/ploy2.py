
class Laptop:
    def build(self):
        print('Laptop Builds..')

class Desktop:
    def build(self):
        print('Desktop building..')
class Alien:
    def code(self, machine : Laptop):
        print("Maching Building..")
        machine.build()
def build_test(test):
    print(test.build())
# laptop = Laptop()
desktop = Desktop()
alien = Alien()
# alien.code(laptop)
alien.code(desktop)


# build_test(laptop)
# build_test(desktop)                