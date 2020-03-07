class Calculator():
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        self.result = a - b
        return self.result
    
    def multiply(self, a, b):
        self.result = a*b
        return self.result

    def division(self, a, b):
        self.result = a/b
        return self.result

    def square(self, a):
        self.result = a**2;
        return self.result

    def square_root(self, a):
        self.result = a**(1/2.0)
        return self.result

