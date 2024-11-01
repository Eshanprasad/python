from abc import ABC, abstractmethod
class Computer(ABC):            # abstract class
    @abstractmethod
    def process(self):          # abstract method
        pass

class Laptop(Computer):         #inheriting abstract class
    def process(self):          # must define all the methods which are parent abstract class, otherwise this class also becomes abstract class
        print("processing")

"""com = Computer()
com.process()"""
#this gives error, coz we can't create an object of abstract class

lap = Laptop()
lap.process()
#output: processing
