from editor import Editor


class ShapeEditor(Editor):
    def __init__(self, canvas):
        super().__init__()
        self.canvas = canvas
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.primitive = None

    def on_button_press(self, event):
        pass

    def on_mouse_drag(self, event):
        pass

    def on_button_release(self, event):
        pass

    def bind_events(self):
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)