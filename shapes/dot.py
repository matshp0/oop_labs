from shape import Shape

class Dot(Shape):
    def __init__(self, canvas, x1, y1):
        super().__init__(canvas, x1, y1)
        self.drawing_conf["fill"] = "black"  # Color of the dot
        self.drawing_conf["outline"] = "black"

        self.initiate()
        self.finished = False

    def initiate(self):
        radius = 2
        self.shape = self.canvas.create_oval(
            self.x1 - radius, self.y1 - radius,
            self.x1 + radius, self.y1 + radius,
            **self.drawing_conf
        )

    def draw(self, x, y):
        pass
