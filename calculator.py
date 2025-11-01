class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b
    
if __name__ == "__main__":
    calc = Calculator()
    print("Addition:", calc.add(10, 10))
    print("Subtraction:", calc.subtract(10, 10))
    print("Multiplication:", calc.multiply(10, 10))
    print("Division:", calc.divide(10, 10))