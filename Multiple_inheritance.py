"""
Method resolution order - MRO
"""
class A:
    def __init__(self):
        self.variable_a = "A value"
        print("in A init")

    def feature(self):            # same method is also available in class B
        print("in A feature")
class B:
    def __init__(self):
        self.variable_b = "B value"
        print("in B init")

    def feature(self):              # same method is also available in class A
        print("in B feature")

class C(B, A):
    def __init__(self):
        print("in C init")

objC = C()
objC.feature()     #calls feature method in B according to method resolution order MRO

"""
output:
in C init
in B feature
"""
