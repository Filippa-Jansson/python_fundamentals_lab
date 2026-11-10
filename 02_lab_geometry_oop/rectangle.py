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
    
    def __eq__(self, other: object) -> bool:
        """Return True if other is a Rectangle with the same width and height."""
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        return False
    
    def __repr__(self) -> str:
        """Return a developer-friendly representation of the rectangle."""
        return f"Rectangle(x={self.x}, y={self.y}, width={self.width}, height={self.height})"
    
    def __str__(self) -> str:
        """Return a user-friendly description of the rectangle."""
        return f"Rectangle centered at ({self.x}, {self.y}) with width={self.width} and height={self.height}"

  
    def plot(self) -> None:
        """Plot the rectangle at its position using matplotlib."""
        fig, ax = plt.subplots()

        # Matplotlib draws rectangles from the bottom-left corner, not the center
        corner_x = self.x - self.width / 2
        corner_y = self.y - self.height / 2

        rect = RectanglePatch(
            (corner_x, corner_y),
            width=self.width,
            height=self.height,
            edgecolor='blue',
            facecolor='lightblue',
        )
        ax.add_patch(rect)

        # Fit the axes around the rectangle with some margin
        margin = 1
        ax.set_xlim(self.x - self.width / 2 - margin, self.x + self.width / 2 + margin)
        ax.set_ylim(self.y - self.height / 2 - margin, self.y + self.height / 2 + margin)

        ax.set_aspect('equal')
        plt.grid(True)
        plt.title(str(self))
        plt.show()