import math

## Code aims to find the width and height of a rectangle, calculate its area, and compare two rectangles.

class Rectangle():
    # Create the constructor "__init__" method
    # Set width and height
    # YOUR CODE HERE
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Create the "__str__" method
    # Set the return value to a string that describes the rectangle
    # YOUR CODE HERE
    def __str__(self):
        return f"Width = {self.width}, height = {self.height}"

    # Create the "area_calculator" method
    # Calculates the area of the rectangle
    # YOUR CODE HERE
    def area_calculator(self):
        area = self.width * self.height
        return area

    # Create the "__eq__" method
    # Returns a boolean value, true if self.width equals other.width and self.height equals other.height
    # YOUR CODE HERE
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            if self.width == other.width and self.height == other.height:
                return True
            else:
                return False
        else:
            return False

def main():
    # steps:
    # call the __str__ method
    # call the area_calculator method
    # call the __eq__ method
    
    # setting the rectangle dimensions
    r1 = Rectangle(10, 8)
    r2 = Rectangle(11, 4)
    r3 = Rectangle(5, 6)

    # r1
    print(r1)
    print(f"Area = {r1.area_calculator()}")

    # r2
    print(r2)
    print(f"Area = {r2.area_calculator()}")

    # are r1 and r2 the same?
    print(r1 == r2)

    # you can create additional rectangle objects to 
    # test your code or learn more about how the class behaves
    pass

if __name__ == "__main__":
    main()