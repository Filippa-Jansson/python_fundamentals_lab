# Here I import the Shape class from shape.py to create the Rectangle class that inherits from it.
from shape import Shape
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as RectanglePatch

# Here I create the Rectangle class that inherits from the Shape class.
class Rectangle(Shape):
    # Here i define the constructor for the Rectangle class with default x, y coordinates, width, and height.
    def __init__(self, x=0, y=0, width=1, height=1):

        # Here i call the constructor of the parent Shape class to initialize x and y.
        super().__init__(x, y)

        # Here i validate that width and height are numeric and positive.
        if not (isinstance(width, (int, float)) and isinstance(height, (int, float))):
            raise TypeError("width and height must be numeric values (int or float).")
        
        # Here i validate that width and height are positive.
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be positive.")
        self.width = width
        self.height = height

    # Here i define the area property to calculate the area of the rectangle.
    @property
    def area(self):
        return self.width * self.height
    
    # Here i define the perimeter property to calculate the perimeter of the rectangle.
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    # Here i define a method to check if the rectangle is a square.
    def is_square(self):
        return self.width == self.height
    
    # Here i define the equality method to compare two Rectangle objects based on their width and height.
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        return False
    
    # Here i define the less-than method to compare two Rectangle objects based on their area.
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area
        raise TypeError("Can only compare Rectangle with Rectangle.")
    
    # Here i define the less-than-or-equal-to, greater-than, and greater-than-or-equal-to methods.
    def __le__(self, other): return self == other or self < other
    def __gt__(self, other): return not self <= other
    def __ge__(self, other): return not self < other

    # Here i define the __repr__ method to provide a string representation of the Rectangle object for debugging.
    def __repr__(self):
        return f"Rectangle(x={self.x}, y={self.y}, width={self.width}, height={self.height})"
    
    # Here i define the __str__ method to provide a user-friendly string representation of the Rectangle object.
    def __str__(self):
        return f"Rectangle centered at ({self.x}, {self.y}) with width={self.width} and height={self.height}"
  

    def plot(self):
        fig, ax = plt.subplots()
        rect = RectanglePatch((0.2, 0.2), width=0.5, height=0.3, edgecolor='blue', facecolor='lightblue')
        ax.add_patch(rect)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_aspect('equal')
        plt.grid(True)
        plt.title('Rectangle')
        plt.show()