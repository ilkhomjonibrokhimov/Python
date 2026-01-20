import math

class Vector:
    def __init__(self, *components):
        if len(components) == 0:
            raise ValueError("Vector must have at least one component")
        self.components = tuple(components)

    def __repr__(self):
        return f"Vector{self.components}"

    def __len__(self):
        return len(self.components)

    def _check_dimension(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Operation only supported between Vectors")
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension")

    # Vector addition
    def __add__(self, other):
        self._check_dimension(other)
        return Vector(*[a + b for a, b in zip(self.components, other.components)])

    # Vector subtraction
    def __sub__(self, other):
        self._check_dimension(other)
        return Vector(*[a - b for a, b in zip(self.components, other.components)])

    # Dot product OR scalar multiplication
    def __mul__(self, other):
        if isinstance(other, Vector):
            self._check_dimension(other)
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector(*[a * other for a in self.components])
        else:
            raise TypeError("Unsupported operand type")

    # Scalar multiplication from left: 3 * v
    def __rmul__(self, scalar):
        return self * scalar

    # Magnitude (length)
    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    # Normalize (unit vector)
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(*[a / mag for a in self.components])
