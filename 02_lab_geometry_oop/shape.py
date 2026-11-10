
# Here I create the base Shape class that will be inherited by other shapes like Rectangle and Circle.
class Shape:
    # Here i define the constructor for the Shape class with default x and y coordinates. it validates that x and y are numeric.
    def __init__(self, x=0, y=0):
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            raise TypeError("x and y must be numeric values (int or float).")
        self.x = x
        self.y = y
    # here i define the translate method to move the shape by dx and dy.
    def translate(self, dx, dy):
        """Move the shape by dx and dy."""
        if not (isinstance(dx, (int, float)) and isinstance(dy, (int, float))):
            raise TypeError("dx and dy must be numeric values (int or float).")
        self.x += dx
        self.y += dy
    # Here i define the __repr__ method to provide a string representation of the Shape object for debugging.
    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"
    # Here i define the __str__ method to provide a user-friendly string representation of the Shape object.
    def __str__(self):
        return f"{self.__class__.__name__} centered at ({self.x}, {self.y})"
