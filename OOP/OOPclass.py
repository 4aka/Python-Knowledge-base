from OOP import Extendable


class OOPclass(Extendable):

    # fields
    SOME_NUM = ''
    SOME_VAR = 0
    field1 = ''
    field2 = ''

    # constructors
    # __init__
    # __str__
    # __repr__
    # __call__
    # __getitem__
    # __setattr__

    def someDef(self, myDict):
        self.field1 = myDict["field1"]
        self.field2 = myDict["field2"]

# The __str__() function controls what should be
# returned when the class object is represented as a string.
    def __str__(self):
        return f"{self.field1}({self.field2})"

    @staticmethod
    def function1():
        print()

    @staticmethod
    def function2(self):
        pass
