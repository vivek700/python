class Calculator:

    def __init__(self,a):
        self.a = a
        # print("Calculaor is created")

    def square(self):
        print(f"The square of {self.a} is {self.a*self.a}")

    def cube(self):
        print(f"The cube of {self.a} is {self.a**3}")   

    def squareRoot(self):
        print(f"The square of {self.a} is {self.a**0.5}")    


a=Calculator(int(input("Enter the number: ")))        
a.square()
a.cube()
a.squareRoot()