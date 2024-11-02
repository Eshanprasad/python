"""python automatically deletes objects even if we dont methoddefine __del__ , but we can delete them manually whenever we want to delete them in the code.
we need to use
del <object name>

we don't have to define __del__ to delete an object. In the above case we are using print statement in __del__ just to uinderstand when the object is being deleted.
"""


class Person:
    def __init__(self, name, age):      #constructor
        self.name = name
        self.age = age

    def __del__(self):      #destructor
        print("object is being deconstructed!")

p = Person("Mike", 20)
print(p)                        #prints object reference
del p                           #deletes object
print(p)                        #NameError: name 'p' is not defined

"""
output:
<__main__.Person object at 0x000001B39E7294F0>
object is being deconstructed!
Traceback (most recent call last):
  File "C:\Users\eshan.prasad.baikan\PycharmProjects\pythonProject\.venv\eshan.py", line 20, in <module>
    print(p)                        #NameError: name 'p' is not defined
          ^
NameError: name 'p' is not defined
"""
