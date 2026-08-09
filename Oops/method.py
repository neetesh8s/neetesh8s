

class computer:

    brand = 'Neetesh AI' # This is a class variable

    def __init__(self, cpu, ram, ssd): #self is mandatory for all method
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd

    @classmethod # usaing classmethod decoratoe to make info() as class method
    def info(cls):
        return cls.brand
    
    def config(self):
        #print("config :", self.cpu, self.ram, self.ssd)
        #or
        return f"config : {self.cpu}, {self.ram}, {self.ssd}"

    @staticmethod
    def gb_to_byte(gb):
        return gb * (1024 ** 3)
    
com1 = computer("i5", '16GB', '1TB')
com2 = computer("i7", '32GB', '2TB')

# com1.config()
# com2.config()
print(com1.config())
print(com2.config())
print(computer.info())
print(computer.gb_to_byte(16))
