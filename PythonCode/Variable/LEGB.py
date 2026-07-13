##The LEGB rule in Python defines how variable names are resolved: Python looks
# for a name in the order Local → Enclosing → Global → Built‑in. This hierarchy 
# ensures that the most specific scope is checked first before moving outward.

x = "global x"
def outer():
    x = "enclosing x"
    def inner():
        x = "local x"
        print(x)   # Local scope
    inner()
    print(x)       # Enclosing scope

outer()
print(x)           # Global scope
print(len([1,2,3])) # Built-in scope