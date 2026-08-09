
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f'{self.name} : {self.balance}'

    def __add__(self, other):
        return Account('combined', self.balance + other.balance)

    def __gt__(self, other):
        return self.balance > other.balance
    
user1 = Account('Test1', 4000)
user2 = Account('Test2', 2000)
print(user1)  
print(user2) 
combined = user1 + user2
print(combined)     

if user1 > user2:  #if want to compare object then we need to call __gt() in call 
    print('Test1 Pay the bill')
else:
    print('Test2 Pay the bill')    