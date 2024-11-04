# Encapsulation
class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    def __repr__(self):
        return f"Name:{self.__name}, Age:{self.__age}, Gender:{self.__gender}"

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name


p1 = Person("eshan", 22, "M")
print(p1)               #prints: Name:eshan, Age:22, Gender:M
print(p1.getName())     #prints: eshan
p1.setName("Mike")      #sets name = Mike
print(p1)               #prints: Name:Mike, Age:22, Gender:M
