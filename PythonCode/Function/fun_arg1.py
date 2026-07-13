
def person(name, age):
    print("Name :", name)
    print('Age :', age)
person('Neetesh', 35)
person(30, 'Neetesh')    
person(name = 'Neetesh', age = '35') # Keyword argument

# multi Keyword argument function. ** will take value as dictionary for ramaining value 
print('===================================')
def person1(name, **keywordArgument):
    print("Name :", name)
    for k,v in keywordArgument.items():
        print(k, " : " ,v)
   
person1(name = 'Neetesh', age = '35', loc = 'Blr', tech = 'AI')