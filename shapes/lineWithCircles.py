from shapes import Line


class LineWithCircles(Line):
    def __init__(self, canvas, x1, y1, circle_radius=10):
        super().__init__(canvas, x1, y1)
        self.drawing_conf["outline"] = "black"
        self.drawing_conf["fill"] = "white"
        self.circle_radius = circle_radius

        self.circle1 = self.canvas.create_oval(
            self.x1 - self.circle_radius, self.y1 - self.circle_radius,
            self.x1 + self.circle_radius, self.y1 + self.circle_radius,
            **self.drawing_conf
        )
        self.circle2 = self.canvas.create_oval(
            self.x1 - self.circle_radius, self.y1 - self.circle_radius,
            self.x1 + self.circle_radius, self.y1 + self.circle_radius,
            **self.drawing_conf
        )

        self.components.extend([self.circle1, self.circle2])

    def draw(self, x, y):
        super().draw(x, y)

        self.canvas.coords(
            self.circle1,
            self.x1 - self.circle_radius, self.y1 - self.circle_radius,
            self.x1 + self.circle_radius, self.y1 + self.circle_radius
        )
        self.canvas.coords(
            self.circle2,
            self.x2 - self.circle_radius, self.y2 - self.circle_radius,
            self.x2 + self.circle_radius, self.y2 + self.circle_radius
        )