def mydecorator(hello):
    def wrapper():
        print("decoraating the function")
        hello()
    return wrapper

@mydecorator
def hello():
    print("Hello_world")

hello()

"""
output:
decoraating the function
Hello_world
"""
