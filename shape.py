class Shape:
    def __init__(self, canvas, x1, y1, x2=None, y2=None):
        self.canvas = canvas
        self.components = []
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2 if x2 is not None else x1
        self.y2 = y2 if y2 is not None else y1
        self.drawing_conf = {
            "width": 4,
            "dash": True
        }

    def draw(self, x, y):
        pass

    def initiate(self):
        pass

    def update_config(self):
        for component in self.components:
            self.canvas.itemconfig(component, **self.drawing_conf)

    def settle(self):
        self.drawing_conf["dash"] = ()
