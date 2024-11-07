class MyEditor:
    editor_instance = None

    def __init__(self, canvas):
        if MyEditor.editor_instance is None:
            self.canvas = canvas
            self.shapes = []
            self.current_tool = None
            self.current_shape = None
            self.bind_events(canvas)
            MyEditor.editor_instance = self
        else:
            raise Exception("MyEditor is already instantiated. Use the global instance.")

    @staticmethod
    def get_instance():
        if MyEditor.editor_instance is None:
            raise Exception("MyEditor has not been initialized yet.")
        return MyEditor.editor_instance

    def set_tool(self, tool):
        self.current_tool = tool

    def on_button_press(self, event):
        self.current_shape = self.current_tool(self.canvas, event.x, event.y)

    def on_mouse_drag(self, event):
        self.current_shape.draw(event.x, event.y)

    def on_button_release(self, event):
        self.current_shape.settle()
        self.current_shape.update_config()
        self.current_shape = None

    def bind_events(self, canvas):
        canvas.bind("<ButtonPress-1>", self.on_button_press)
        canvas.bind("<B1-Motion>", self.on_mouse_drag)
        canvas.bind("<ButtonRelease-1>", self.on_button_release)