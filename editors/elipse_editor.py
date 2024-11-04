from shape_editor import ShapeEditor
from shapes.elipse import Elipse


class ElipseEditor(ShapeEditor):
    def __init__(self, canvas):
        super().__init__(canvas)

    def on_button_press(self, event):
        self.x1 = event.x
        self.y1 = event.y
        self.x2 = event.x
        self.y2 = event.y

        self.primitive = Elipse(self.canvas, self.x1, self.y1, self.x2, self.y2)
        self.primitive.draw()

    def on_mouse_drag(self, event):
        self.x2 = event.x
        self.y2 = event.y

        self.primitive.move(self.x1 - (self.x2 - self.x1), self.y1 - (self.y2 - self.y1), self.x2, self.y2)

    def on_button_release(self, event):
        self.primitive.finished = True
        self.primitive.draw()

