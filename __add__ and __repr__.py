class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):                                   # + operator overloading
        return Vector(self.x + other.x, self.y + other.y)
    
    def __repr__(self):                                         # defines what need's to be printed when we try to print an object
        return f"X:{self.x}, Y:{self.y}"

v1 = Vector(10, 20)
v2 = Vector(50, 60)
v3 = v1+v2
print(v3)

"""
output:
X:60, Y:80
"""
