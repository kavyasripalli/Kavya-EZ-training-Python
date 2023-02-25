class parent():
    # Constructor
    def __init__(self):
        self.value = "Inside Parent"

    # Parent a show method
    def show(self):
        print(self.value)

# Defining child class
class Child(parent):

    # Constructor
    def __init__(self):
        self.value = "Inside Child"

    # Child a show method
    def show(self):
        print(self.value)
obj1 = parent()
obj2 = Child()
obj1.show()
obj2.show()
