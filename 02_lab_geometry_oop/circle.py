from shape import Shape
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle as CirclePatch

class Circle(Shape):
    """A class representing a circle."""
    def __init__(self, x: float = 0, y: float = 0, radius: float = 1) -> None:
        """Create a circle with center (x, y) and the given radius."""
        super().__init__(x, y)
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be numeric")
        if radius <= 0:
            raise ValueError("radius must be positive")
        self.radius = radius

    @property
    def area(self) -> float:
        """Return the area of the circle."""
        return math.pi * self.radius ** 2
    
    @property
    def perimeter(self) -> float:
        """Return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius
    
    def is_unit_circle(self) -> bool:
        """Return True if the circle is a unit circle (radius = 1), False otherwise."""
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
    
    def __repr__(self) -> str:
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius})"
    
    # Here i define the __str__ method to provide a user-friendly string representation of the Circle object.
    def __str__(self) -> str:
        return f"Circle with center ({self.x}, {self.y}) and radius {self.radius}"


    def plot(self) -> None:
        """Plot the circle using matplotlib."""
        fig, ax = plt.subplots()
        circle = CirclePatch((0.5, 0.5), radius=0.2, edgecolor='red', facecolor='lightcoral')
        ax.add_patch(circle)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_aspect('equal')
        plt.grid(True)
        plt.title('Circle')
        plt.show()