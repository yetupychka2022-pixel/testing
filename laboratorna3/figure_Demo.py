class Figure:
    def __init__(self, type, length) -> None:
        assert length > 0, "Length must be greater than 0!"
        assert type in ["square", "rectangle", "triangle"], "Allowed figures: square, rectangle, triangle"
        self.type = type
        self.length = length

a = Figure("trapezoid", 12)
b = Figure("square", 0)
c = Figure("square", 1)
print("Object c created:", c.type, c.length)
