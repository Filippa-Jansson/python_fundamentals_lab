# here i import the Shape class and the math module to use mathematical functions.
from shape import Shape
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle as CirclePatch

# Here i create the Circle class that inherits from the Shape class.
class Circle(Shape):
    def __init__(self, x=0, y=0, radius=1):
        super().__init__(x, y)
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be numeric")
        if radius <= 0:
            raise ValueError("radius must be positive")
        self.radius = radius

    # Here i define the area property to calculate the area of the circle.
    @property
    def area(self):
        return math.pi * self.radius ** 2
    
    # Here i define the perimeter property to calculate the perimeter of the circle.
    @property
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    # Here i define a method to check if the circle is a unit circle.
    def is_unit_circle(self):
        return self.radius == 1
    
    # Here i define the equality method to compare two Circle objects based on their radius.
    def __eq__(self, other):
        return isinstance(other, Circle) and self.radius == other.radius
    
    # Here i define the less-than method to compare two Circle objects based on their radius.
    def __lt__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("Can only compare Circle with Circle")
        return self.radius < other.radius
    
    # Here i define the less-than-or-equal-to, greater-than, and greater-than-or-equal-to methods.
    def __le__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("Can only compare Circle with Circle")
        return self.radius <= other.radius
    
    # Here i define the less-than-or-equal-to, greater-than, and greater-than-or-equal-to methods.
    def __gt__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("Can only compare Circle with Circle")
        return self.radius > other.radius
    
    # Here i define the less-than-or-equal-to, greater-than, and greater-than-or-equal-to methods.
    def __ge__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("Can only compare Circle with Circle")
        return self.radius >= other.radius
    
    # Here i define the __repr__ method to provide a string representation of the Circle object for debugging.
    def __repr__(self):
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius})"
    
    # Here i define the __str__ method to provide a user-friendly string representation of the Circle object.
    def __str__(self):
        return f"Circle with center ({self.x}, {self.y}) and radius {self.radius}"


    def plot(self):
        fig, ax = plt.subplots()
        circle = CirclePatch((0.5, 0.5), radius=0.2, edgecolor='red', facecolor='lightcoral')
        ax.add_patch(circle)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_aspect('equal')
        plt.grid(True)
        plt.title('Circle')
        plt.show()