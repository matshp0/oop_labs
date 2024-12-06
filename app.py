import tkinter as tk
from shapes import Elipse, Rectangle, Line, Dot, LineWithCircles, Cube
from tkinter import Menu, Button, Toplevel, PhotoImage
from myEditor import MyEditor
from Toolbar import Toolbar
from MyTable import MyTable
from ObservableList import ObservableList


class App:
    def __init__(self, root):
        self.start_x = None
        self.current_shape = None
        self.root = root
        self.shapes = ObservableList([])
        self.table = MyTable(root, self.shapes)
        self.root.title("Lab5")

        menu_bar = Menu(root)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_table)  # Open table command
        file_menu.add_command(label="Save")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        menu_bar.add_cascade(label="Файл", menu=file_menu)

        objects_menu = Menu(menu_bar, tearoff=0)
        objects_menu.add_command(label="Лінія", command=lambda: self.editor.set_tool(Line))
        objects_menu.add_command(label="Точка", command=lambda: self.editor.set_tool(Dot))
        objects_menu.add_command(label="Прямокутник", command=lambda: self.editor.set_tool(Rectangle))
        objects_menu.add_command(label="Еліпс", command=lambda: self.editor.set_tool(Elipse))
        objects_menu.add_command(label="Відрізок з колами", command=lambda: self.editor.set_tool(LineWithCircles))
        objects_menu.add_command(label="Куб", command=lambda: self.editor.set_tool(Cube))
        menu_bar.add_cascade(label="Об'єкти", menu=objects_menu)

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About")
        menu_bar.add_cascade(label="Довідка", menu=help_menu)
        root.config(menu=menu_bar)

        self.toolbar = Toolbar(root, self)
        self.canvas = tk.Canvas(root, bg="white", width=1200, height=900)
        self.canvas.pack()
        MyEditor(self.canvas, self.shapes)
        self.editor = MyEditor.get_instance()
        self.editor.set_tool(Elipse)

    def show_popup(self, tool_name):
        popup = Toplevel(self.root)
        popup.wm_overrideredirect(True)
        popup.geometry(f"+{self.root.winfo_x() + 100}+{self.root.winfo_y() + 50}")
        label = tk.Label(popup, text=f"Обрано: {tool_name}", bg="lightyellow", relief=tk.SOLID, borderwidth=1)
        label.pack()

        self.root.after(1000, popup.destroy)

    def open_table(self):
        self.table.show_window()

    def close_table(self):
        self.table.hide_window()
