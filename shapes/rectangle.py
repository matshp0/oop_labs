from shape import Shape


class Rectangle(Shape):
    def __init__(self, canvas, x1, y1, x2, y2):
        super().__init__(canvas, x1, y1, x2, y2)
        self.rect = None
        self.finished = False

    def draw(self):
        if self.finished:
            self.rect = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill="light blue", outline="black", width=3)
        else:
            self.rect = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill="light blue", outline="blue", width=3)

    def move(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas.coords(self.rect, self.x1, self.y1, self.x2, self.y2)
