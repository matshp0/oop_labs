from shape import Shape


class Dot(Shape):
    def __init__(self, canvas, x1, y1, radius=2):
        super().__init__(canvas, x1, y1)
        self.radius = radius
        self.drawing_conf["fill"] = "black"
        self.components.append(self.canvas.create_oval(
            self.x1 - self.radius, self.y1 - self.radius,
            self.x1 + self.radius, self.y1 + self.radius,
            **self.drawing_conf
        ))

    def draw(self, x, y):
        pass
