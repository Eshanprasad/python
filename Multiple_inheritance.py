"""
In Class C, if we want to also execute super class init method, we need to use super()
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
        super().__init__()          #this calls init method of class B according to MRO
        print("in C init")

objC = C()

"""
output:
in B init
in C init
"""
