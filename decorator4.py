"""suppose if our hello function takes an orgument ex: name,
then the existing wrapper function in decorator just calls the method hello(), without passing argument to hello function, which results in error

to tackle this, we need to use *args
"""

def mydecorator(hello):
    def wrapper(*args):
        print("decoraating the function")
        hello(*args)
    return wrapper

@mydecorator
def hello(name):
    print(f"Hello {name}!")

hello("Eshan")

"""
output:
decoraating the function
Hello Eshan!
"""
