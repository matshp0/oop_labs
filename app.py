import tkinter as tk
from tkinter import Menu
from editors.rectangle_editor import RectangleEditor
from editors.elipse_editor import ElipseEditor
from editors.line_editor import LineEditor
from editors.dot_editor import DotEditor

class App:
    def __init__(self, root):
        self.start_x = None
        self.current_shape = None
        self.root = root
        self.root = root
        self.root.title("Lab2")

        # Add "File" menu
        menu_bar = Menu(root)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        menu_bar.add_cascade(label="Файл", menu=file_menu)

        # Add "Objects" menu
        objects_menu = Menu(menu_bar, tearoff=0)
        objects_menu.add_command(label="Лінія", command=self.set_tool_line)
        objects_menu.add_command(label="Точка", command=self.set_tool_dot)
        objects_menu.add_command(label="Прямокутник", command=self.set_tool_rectangle)
        objects_menu.add_command(label="Еліпс", command=self.set_tool_elipse)
        menu_bar.add_cascade(label="Об'єкти", menu=objects_menu)

        # Add "Help" menu
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About")
        menu_bar.add_cascade(label="Довідка", menu=help_menu)
        root.config(menu=menu_bar)
        # Create a canvas for drawing
        self.canvas = tk.Canvas(root, bg="white", width=1500, height=1000)
        self.canvas.pack()

        self.rect_editor = RectangleEditor(self.canvas)
        self.elipse_editor = ElipseEditor(self.canvas)
        self.line_editor = LineEditor(self.canvas)
        self.dot_editor = DotEditor(self.canvas)

    def set_tool_rectangle(self):
        self.root.title("Прямокутник")
        self.current_shape = self.rect_editor
        self.current_shape.bind_events()

    def set_tool_elipse(self):
        self.root.title("Еліпс")
        self.current_shape = self.elipse_editor
        self.current_shape.bind_events()

    def set_tool_line(self):
        self.root.title("Лінія")
        self.current_shape = self.line_editor
        self.current_shape.bind_events()

    def set_tool_dot(self):
        self.root.title("Точка")
        self.current_shape = self.dot_editor
        self.current_shape.bind_events()



