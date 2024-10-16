"""
Accessing class and instance variables of Parent class.
Correcting constructor of class C to access instance variables of A and B
"""
class A:
    class_variable_a = "class A value"
    def __init__(self):
        self.instance_variable_a = "instance A value"
        print("in A init")

    def feature(self):            # same method is also available in class B
        print("in A feature")
class B:
    class_variable_B = "class B value"
    def __init__(self):
        self.instance_variable_b = "instance B value"
        print("in B init")

    def feature(self):              # same method is also available in class A
        print("in B feature")

class C(B, A):
    def __init__(self):
        B.__init__(self)  # Call B's initializer
        A.__init__(self)  # Call A's initializer
        print("in C init")

objC = C()
print(objC.class_variable_a)
print(objC.class_variable_B)
print(objC.instance_variable_a)  
print(objC.instance_variable_b)     

"""
output:
in B init
in A init
in C init
class A value
class B value
instance A value
instance B value

"""
