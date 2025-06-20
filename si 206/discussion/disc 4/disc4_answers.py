import math

## Code aims to find the width and height of a rectangle, calculate its area, and compare two rectangles.

class Rectangle():
    # Create the constructor "__init__" method
    # This is initializing the rectangle class, saying every rectangle will have a width and height
    # YOUR CODE HERE
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Create the "__str__" method

    # YOUR CODE HERE
    def __str__(self):
        return f"Rectangle(width = {self.width}, height = {self.height})"

    # Create the "area_calculator" method

    # YOUR CODE HERE
    def area_calculator(self):
        return self.width * self.height

    # Create the "__eq__" method
    # 
    # Returns a boolean value

    # YOUR CODE HERE
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        return False
    

def main():
    r1 = Rectangle(10, 10)
    # call the __str__ method
    print(r1)
    # call the area_calculator method
    print("Area:", r1.area_calculator())


    r2 = Rectangle(10, 15)
    print(r2)
    print("Area:", r2.area_calculator())
    # call the __eq__ method
    print(r1 == r2)
    print()

    # you can create additional rectangle objects to 
    # test your code or learn more about how the class behaves
    pass

if __name__ == "__main__":
    main()