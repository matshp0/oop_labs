from shape_editor import ShapeEditor
from shapes.dot import Dot  # Import the Dot class


class DotEditor(ShapeEditor):
    def __init__(self, canvas):
        super().__init__(canvas)

    def on_button_press(self, event):
        self.x1 = event.x
        self.y1 = event.y

        self.primitive = Dot(self.canvas, self.x1, self.y1)
        self.primitive.draw()

    def on_mouse_drag(self, event):
        self.primitive.move(event.x, event.y)

    def on_button_release(self, event):
        self.primitive.finished = True
        self.primitive.draw()