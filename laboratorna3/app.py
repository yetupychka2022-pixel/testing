class Figure:
    FIGURES = ["square", "rectangle", "triangle"]

    def __init__(self, type, length) -> None:
        assert length > 0, "Length must be greater than 0!"
        assert type in self.FIGURES, "Allowed figures: square, rectangle, triangle"
        self.type = type
        self.length = length

    @property
    def get_figure_type(self):
        return self.type

    @property
    def get_figure_length(self):
        return self.length

    @property
    def get_angles(self):
        if self.type in ["square", "rectangle"]:
            return 4
        if self.type == "triangle":
            return 3


def test_app_triangle():
    fig = "triangle"
    triangle = Figure(fig, 4)
    assert triangle.type == fig
