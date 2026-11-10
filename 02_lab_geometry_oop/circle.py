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
    
    def __eq__(self, other: object) -> bool:
        """Return True if other is a Circle with the same radius."""
        return isinstance(other, Circle) and self.radius == other.radius
        
    def __repr__(self) -> str:
        """Return a developer-friendly representation of the circle."""
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius})"
    
    def __str__(self) -> str:
        """Return a user-friendly description of the circle."""
        return f"Circle with center ({self.x}, {self.y}) and radius {self.radius}"


    def plot(self) -> None:
        """Plot the circle at its position using matplotlib."""
        fig, ax = plt.subplots()
        circle = CirclePatch(
            (self.x, self.y),
            radius=self.radius,
            edgecolor='red',
            facecolor='lightcoral',
        )
        ax.add_patch(circle)

        # Fit the axes around the circle with some margin
        margin = 1
        ax.set_xlim(self.x - self.radius - margin, self.x + self.radius + margin)
        ax.set_ylim(self.y - self.radius - margin, self.y + self.radius + margin)

        ax.set_aspect('equal')
        plt.grid(True)
        plt.title(str(self))
        plt.show()