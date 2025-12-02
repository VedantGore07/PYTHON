# 4. Create a base class called Shape with a method area() that returns 0.
#  Create derived class called Rectangle that inherits from shape and overrides
#  the area() method to calculate and return the area of a rectangle.

class Shape():
    def area(self):
        return 0
    
s1 = Shape()
s1.area()
print("Area of shape")

class Rectangle(Shape):
    def area(self):
        l = 10
        b = 20
        print(l*b)

r1 = Rectangle()
r1.area()

