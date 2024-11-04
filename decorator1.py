def mydecorator(hello):
    def wrapper():
        print("decoraating the function")
        hello()
    return wrapper
def hello():
    print("Hello_world")
mydecorator(hello)()


"""
output:
decoraating the function
Hello_world
"""
