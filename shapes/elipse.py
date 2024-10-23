from shape import Shape


class Elipse(Shape):
    def __init__(self, canvas, x1, y1, x2, y2):
        super().__init__(canvas, x1, y1, x2, y2)
        self.ellipse = None
        self.finished = False

    def draw(self):
        if self.finished:
            self.ellipse = self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="grey", outline="black", width=3)
        else:
            self.ellipse = self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="grey", outline="red", width=3)

    def move(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas.coords(self.ellipse, self.x1, self.y1, self.x2, self.y2)