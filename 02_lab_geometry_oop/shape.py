class Shape:
    """A base class representing a geometric shape."""
    def __init__(self, x: float = 0, y: float = 0) -> None:
        """Create a shape with center (x, y)."""
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            raise TypeError("x and y must be numeric values (int or float).")
        self.x = x
        self.y = y

    def translate(self, dx: float, dy: float) -> None:
        """Move the shape by dx and dy."""
        if not (isinstance(dx, (int, float)) and isinstance(dy, (int, float))):
            raise TypeError("dx and dy must be numeric values (int or float).")
        self.x += dx
        self.y += dy
   
    def __repr__(self) -> str:
        """Return a developer-friendly representation of the shape."""
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"
    
    def __str__(self) -> str:
        """Return a user-friendly description of the shape."""
        return f"{self.__class__.__name__} centered at ({self.x}, {self.y})"
    
    @property
    def area(self) -> float:
        """Return the area of the shape. Implemented by each subclass."""
        raise NotImplementedError("Subclasses must implement area")

    def _check_comparable(self, other: object) -> None:
        """Raise TypeError if other is not a Shape."""
        if not isinstance(other, Shape):
            raise TypeError("Can only compare a shape with another shape")

    def __lt__(self, other: "Shape") -> bool:
        """Return True if this shape has a smaller area than other."""
        self._check_comparable(other)
        return self.area < other.area

    def __le__(self, other: "Shape") -> bool:
        """Return True if this shape's area is smaller than or equal to other's."""
        self._check_comparable(other)
        return self.area <= other.area

    def __gt__(self, other: "Shape") -> bool:
        """Return True if this shape has a larger area than other."""
        self._check_comparable(other)
        return self.area > other.area

    def __ge__(self, other: "Shape") -> bool:
        """Return True if this shape's area is larger than or equal to other's."""
        self._check_comparable(other)
        return self.area >= other.area
