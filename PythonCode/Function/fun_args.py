
def add(num1, num2): #default argument function
    return num1+num2
result = add(45, 50)
print(result)

# multi args function. * will take value as tupple for ramaining value 

def add_multi_arrgs(num1, *num2): 
    sum = num1
    for n in num2:
        sum = sum + n
    return sum
result1 =  add_multi_arrgs(10, 20, 30, 40)
print(result1)       