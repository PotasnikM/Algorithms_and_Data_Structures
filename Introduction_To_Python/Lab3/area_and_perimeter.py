from math import pi


# Creating class Triangle
class Triangle:

    # Initializing object
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    # Creating method to calculate area of the triangle
    def area(self):
        s = (self.a + self.b + self.c)/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5

    # Creating method to calculate perimeter of the triangle
    def perimeter(self):
        return self.a + self.b + self.c


# Creating class Square
class Square:

    # Initializing object
    def __init__(self, a):
        self.a = float(a)

    # Creating method to calculate area of the square
    def area(self):
        return self.a ** 2

    # Creating method to calculate perimeter of the square
    def perimeter(self):
        return 4 * self.a


# Creating class Circle
class Circle:

    # Initializing object
    def __init__(self, r):
        self.r = float(r)

    # Creating method to calculate area of the circle
    def area(self):
        return pi * self.r ** 2

    # Creating method to calculate perimeter of the circle
    def perimeter(self):
        return pi * 2 * self.r
