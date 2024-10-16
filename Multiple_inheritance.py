"""
In Class C, if we want to call class B and class A feature methods
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
        super().feature()               #this calls Class B feature method according to MRO. B.feature(self) also works
        A.feature(self)                 # this calls Class A feature method (works even if C doesn't inherit A). but passing "self" in paranthesis is a must.
        print("in C init")

objC = C()

"""
output:
in B feature
in A feature
in C init
"""
