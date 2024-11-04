"""
if hello() function has a returned value rather than print statements, we need to 
return hello(*args) in wrapper function.
print(hello("Eshan"))
"""

def mydecorator(hello):
    def wrapper(*args):
        print("decoraating the function")
        return hello(*args)
    return wrapper

@mydecorator
def hello(name):
    return f"Hello {name}!"

print(hello("Eshan"))
