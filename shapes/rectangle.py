from shape import Shape


class Rectangle(Shape):
    def __init__(self, canvas, x1, y1):
        super().__init__(canvas, x1, y1)
        self.drawing_conf["fill"] = "white"
        self.components.append(self.canvas.create_rectangle(
            self.x1, self.y1, self.x1, self.y1, **self.drawing_conf
        ))

    def draw(self, x, y):
        self.x2 = x
        self.y2 = y
        self.canvas.coords(self.components[0], self.x1, self.y1, self.x2, self.y2)

    def cock(self):
        print("recatangel method")
