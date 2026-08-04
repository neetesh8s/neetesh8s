
class computer:

    def __init__(self, processer, ram, ssd): #self is mandatory for all method
        self.processer = processer
        self.ram = ram
        self.ssd = ssd

    def config(self):
        #print("config :", self.processer, self.ram, self.ssd)
        #or
        return f"config : {self.processer}, {self.ram}, {self.ssd}"

com1 = computer("i5", '16GB', '1TB')
com2 = computer("i7", '32GB', '2TB')

# com1.config()
# com2.config()
print(com1.config())
print(com2.config())