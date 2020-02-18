class MyClass:

    i = 0

    def __init__(self):
        print("Class instantized")

    def sum(self, a, b):
        self.i = a+b
        return self.i
        
        
