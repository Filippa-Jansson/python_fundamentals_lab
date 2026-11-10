from shape import Shape
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as RectanglePatch

class Rectangle(Shape):
    """A class representing a rectangle."""
    def __init__(self, x: float = 0, y: float = 0, width: float = 1, height: float = 1) -> None:
        """Create a rectangle with center (x, y), width, and height."""
        super().__init__(x, y)

        if not (isinstance(width, (int, float)) and isinstance(height, (int, float))):
            raise TypeError("width and height must be numeric values (int or float).")
        
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be positive.")
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        """Return the area of the rectangle."""
        return self.width * self.height
    
    @property
    def perimeter(self) -> float:
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)
    
    def is_square(self) -> bool:
        """Return True if the rectangle is a square (width == height), False otherwise."""
        return self.width == self.height
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        return False
    
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area
        raise TypeError("Can only compare Rectangle with Rectangle.")
    
    def __le__(self, other): return self == other or self < other
    def __gt__(self, other): return not self <= other
    def __ge__(self, other): return not self < other

    def __repr__(self) -> str:
        """Return a developer-friendly representation of the rectangle."""
        return f"Rectangle(x={self.x}, y={self.y}, width={self.width}, height={self.height})"
    
    def __str__(self) -> str:
        """Return a user-friendly description of the rectangle."""
        return f"Rectangle centered at ({self.x}, {self.y}) with width={self.width} and height={self.height}"
  

    def plot(self) -> None:
        """Plot the rectangle using matplotlib."""
        fig, ax = plt.subplots()
        rect = RectanglePatch((0.2, 0.2), width=0.5, height=0.3, edgecolor='blue', facecolor='lightblue')
        ax.add_patch(rect)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_aspect('equal')
        plt.grid(True)
        plt.title('Rectangle')
        plt.show()