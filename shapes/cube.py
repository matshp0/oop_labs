from shape import Shape
from shapes import Line
from shapes import Rectangle


class Cube(Line, Rectangle):
    def __init__(self, canvas, x1, y1):
        super().__init__(canvas, x1, y1)
        self.offset = 45
        self.drawing_conf["fill"] = ""
        self.front_face = self.canvas.create_rectangle(x1, y1, x1, y1, **self.drawing_conf)
        self.back_face = self.canvas.create_rectangle(x1 + self.offset, y1 + self.offset, x1 + self.offset,
                                                      y1 + self.offset, **self.drawing_conf)
        self.drawing_conf["fill"] = "black"
        self.lines = [
            self.canvas.create_line(x1, y1, x1 + self.offset, y1 + self.offset, **self.drawing_conf),
            self.canvas.create_line(x1, y1, x1 + self.offset, y1 + self.offset, **self.drawing_conf),
            self.canvas.create_line(x1, y1, x1 + self.offset, y1 + self.offset, **self.drawing_conf),
            self.canvas.create_line(x1, y1, x1 + self.offset, y1 + self.offset, **self.drawing_conf),
        ]
        self.drawing_conf["fill"] = None
        self.components.extend(self.lines)
        self.components.append(self.front_face)
        self.components.append(self.back_face)

    def draw(self, x, y):
        self.canvas.coords(self.front_face, self.x1, self.y1, x, y)
        self.canvas.coords(self.back_face, self.x1 + self.offset, self.y1 + self.offset, x + self.offset,
                           y + self.offset)
        front_coords = self.canvas.coords(self.front_face)
        back_coords = self.canvas.coords(self.back_face)
        self.canvas.coords(self.lines[0], front_coords[0], front_coords[1], back_coords[0], back_coords[1])
        self.canvas.coords(self.lines[1], front_coords[2], front_coords[1], back_coords[2], back_coords[1])
        self.canvas.coords(self.lines[2], front_coords[0], front_coords[3], back_coords[0], back_coords[3])
        self.canvas.coords(self.lines[3], front_coords[2], front_coords[3], back_coords[2], back_coords[3])