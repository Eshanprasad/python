"""
In Class C, if we want to call Class A init method also
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
        A.__init__(self)              # this calls class A init method. In this case, you are not relying on inheritance. Instead, you are accessing A's method directly. This works even if C is not inheriting A.
        super().__init__()            #this calls init method of class B according to MRO
        print("in C init")

objC = C()

"""
output:
in A init
in B init
in C init
"""
