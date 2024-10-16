"""
Accessing class and instance variables of Parent class
"""
class A:
    class_variable_a = "class A value"
    def __init__(self):
        self.instance_variable_a = "A value"
        print("in A init")

    def feature(self):            # same method is also available in class B
        print("in A feature")
class B:
    class_variable_B = "class B value"
    def __init__(self):
        self.instance_variable_b = "B value"
        print("in B init")

    def feature(self):              # same method is also available in class A
        print("in B feature")

class C(B, A):
    def __init__(self):
        print("in C init")

objC = C()
print(objC.class_variable_a)
print(objC.class_variable_B)
print(objC.instance_variable_a)     #error
print(objC.instance_variable_b)     #error


"""
output:
in C init
class A value
class B value

    print(objC.instance_variable_a)
          ^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'C' object has no attribute 'instance_variable_a'




Explanation:
When you create objC = C(), the following happens:
The __init__ method of C is called.
It prints in C init.
Note that the constructors of A and B are not called because C does not call super().__init__() or directly call B.__init__(self) or A.__init__(self).


print(objC.class_variable_a): This will work because class_variable_a is a class variable in A, and C inherits from A.
print(objC.class_variable_B): This will work because class_variable_B is a class variable in B, and C inherits from B


We get error when executing
print(objC.instance_variable_a)
print(objC.instance_variable_b) because,
constructors of A and B are not called because C does not call super().__init__() or directly call B.__init__(self) or A.__init__(self). Thus instance variables of A and B classes are never initialised

"""
