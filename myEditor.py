class MyEditor:
    _instance = None

    def __new__(cls, canvas, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, canvas, shapes):
        if hasattr(self, '_initialized') and self._initialized:
            return

        self.canvas = canvas
        self.observed_shapes = shapes
        self.shapes = list(shapes)
        self.current_tool = None
        self.current_shape = None
        self.bind_events(canvas)
        self._initialized = True
        self.observed_shapes.on('remove', self.on_remove)

    @staticmethod
    def get_instance():
        if MyEditor._instance is None:
            raise Exception("MyEditor has not been initialized yet.")
        return MyEditor._instance

    def on_remove(self, index):
        shape = self.shapes[index]
        shape.erase()
        del self.shapes[index]

    def set_tool(self, tool):
        self.current_tool = tool

    def on_button_press(self, event):
        self.current_shape = self.current_tool(self.canvas, event.x, event.y)

    def on_mouse_drag(self, event):
        self.current_shape.draw(event.x, event.y)

    def on_button_release(self, event):
        self.current_shape.settle()
        self.current_shape.update_config()
        self.shapes.append(self.current_shape)
        self.observed_shapes.append(self.current_shape)
        self.current_shape = None

    def bind_events(self, canvas):
        canvas.bind("<ButtonPress-1>", self.on_button_press)
        canvas.bind("<B1-Motion>", self.on_mouse_drag)
        canvas.bind("<ButtonRelease-1>", self.on_button_release)
