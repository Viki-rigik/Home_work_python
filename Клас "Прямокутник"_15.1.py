class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        square = self.width * self.height
        print(f"Rectangle area: {square}")
        return square

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        result = self.get_square() == other.get_square()
        print(f"Comparing rectangles: {result}")
        return result

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        new_area = self.get_square() + other.get_square()
        print(f"Sum areas: {new_area}")
        new_width = int(new_area ** 0.5)
        new_height = new_area // new_width
        if new_width * new_height != new_area:
            new_height += 1
        return Rectangle(new_width, new_height)

    def __mul__(self, n):
        if not isinstance(n, (int, float)):
            return NotImplemented
        new_area = int(self.get_square() * n)
        print(f"New area: {new_area}")
        new_width = int(new_area ** 0.5)
        new_height = new_area // new_width
        if new_width * new_height != new_area:
            new_height += 1
        return Rectangle(new_width, new_height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, area={self.get_square()})"

r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

print(r1.get_square())
print(r2.get_square())

r3 = r1 + r2
print(r3)

r4 = r1 * 4
print(r4)

print(Rectangle(3, 6) == Rectangle(2, 9))






