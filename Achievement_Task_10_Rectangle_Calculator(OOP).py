# Name:                     Task 10 – Rectangle_Calculator(OOP)
# Author:                   Yunfeng Lin (Ylin8832)
# Date Created:             March 24, 2023
# Date Last Modified:       March 24, 2023

class Rectangle(): # Define a class Rectangle.
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self): 
        global recArea # global keyword is used in order to use the variable outside the function.
        recArea =self.length * self.width #to calculate the area of a rectangle.
    
    def rectangle_perimeter(self):
        global perimeter # global keyword is used in order to use the variable outside the function.
        perimeter = (self.length * 2) + (self.width * 2)  # To calculate the perimeter of a rectangle.

    def displayInfo(self):
        print("width: {} cm".format(self.width))
        print("Length:{} cm".format(self.length))
        print("\nThe perimeter of the rectangle is",perimeter,"cm")
        print("The area of the rectangle is",recArea,"Square cm")

newRectangle = Rectangle(10, 12)
print("{0:-^50s}".format("Rectangle Calculator"))
newRectangle.width = float(input("\nPlease input the width of the rectangle: "))
newRectangle.length = float(input("Please input the length of the rectangle: "))

Rectangle.rectangle_area(newRectangle)
Rectangle. rectangle_perimeter(newRectangle)
Rectangle.displayInfo(newRectangle)
Rectangle.rectangle_area(newRectangle)
