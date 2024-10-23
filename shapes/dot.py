from shape import Shape


class Dot(Shape):
    def __init__(self, canvas, x, y):
        self.radius = 5  # Radius of the dot
        super().__init__(canvas, x - self.radius, y - self.radius, x + self.radius, y + self.radius)
        self.dot = None
        self.finished = False
        self.x = x
        self.y = y

    def draw(self):
        if self.dot is None:
            self.dot = self.canvas.create_oval(self.x - self.radius, self.y - self.radius,
                                                 self.x + self.radius, self.y + self.radius,
                                                 fill="black")
        else:
            # If the dot is already drawn, update its position
            self.canvas.coords(self.dot, self.x - self.radius, self.y - self.radius,
                               self.x + self.radius, self.y + self.radius)

    def move(self, x, y):
        self.x = x
        self.y = y
        self.x1, self.y1, self.x2, self.y2 = x - self.radius, y - self.radius, x + self.radius, y + self.radius
        self.draw()
