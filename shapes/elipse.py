from shape import Shape


class Elipse(Shape):
    def __init__(self, canvas, x1, y1):
        super().__init__(canvas, x1, y1)
        self.drawing_conf["fill"] = "white"
        self.drawing_conf["outline"] = "blue"
        self.drawing_conf["dash"] = (2, 8)

        self.initiate()
        self.finished = False

    def initiate(self):
        self.shape = self.canvas.create_oval(self.x1, self.y1, self.x1, self.y1, **self.drawing_conf)

    def draw(self, x, y):
        self.x2 = x
        self.y2 = y
        self.canvas.coords(self.shape, self.x1, self.y1, self.x2, self.y2)