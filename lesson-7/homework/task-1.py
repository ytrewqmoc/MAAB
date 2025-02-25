import math

class Vector:
    def __init__(self, *components):
        if not components:
            raise ValueError("A vector must have at least one component.")
        self.components = tuple(float(c) for c in components)

    def __repr__(self):
        return f"Vector{self.components}"
    
    def __add__(self, other):
        if not isinstance(other, Vector) or len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension for addition.")
        return Vector(*[a + b for a, b in zip(self.components, other.components)])
    
    def __sub__(self, other):
        if not isinstance(other, Vector) or len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension for subtraction.")
        return Vector(*[a - b for a, b in zip(self.components, other.components)])
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*[a * other for a in self.components])
        elif isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must be of the same dimension for dot product.")
            return sum(a * b for a, b in zip(self.components, other.components))
        else:
            raise TypeError("Multiplication is only supported with scalars or other vectors.")
    
    def __rmul__(self, other):
        return self * other
    
    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*[a / mag for a in self.components])
    
    def to_list(self):
        return list(self.components)

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print("v1:", v1)
print("v2:", v2)
print("Addition:", v1 + v2)
print("Subtraction:", v1 - v2)
print("Dot Product:", v1 * v2)
print("Scalar Multiplication:", 3 * v1)
print("Magnitude of v1:", v1.magnitude())
print("Normalized v1:", v1.normalize())