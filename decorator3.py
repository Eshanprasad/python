"""suppose if our hello function takes an orgument ex: name,
then the existing wrapper function in decorator just calls the method hello(), without passing argument to hello function, which results in error"""

def mydecorator(hello):
    def wrapper():
        print("decoraating the function")
        hello()
    return wrapper

@mydecorator
def hello(name):
    print(f"Hello {name}!")

hello("Eshan")

"""
output:
TypeError: mydecorator.<locals>.wrapper() takes 0 positional arguments but 1 was given
"""
