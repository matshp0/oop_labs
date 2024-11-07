import tkinter as tk
from shapes import Elipse, Rectangle, Line, Dot, LineWithCircles, Cube
from tkinter import Menu, Button, Toplevel, PhotoImage
from myEditor import MyEditor


class Toolbar:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.toolbar_frame = tk.Frame(parent)
        self.toolbar_frame.pack(side=tk.TOP, fill=tk.X)

        self.line_icon = PhotoImage(file="icons/line.png")
        self.dot_icon = PhotoImage(file="icons/dot.png")
        self.rectangle_icon = PhotoImage(file="icons/rectangle.png")
        self.elipse_icon = PhotoImage(file="icons/elipse.png")
        self.cube_icon = PhotoImage(file="icons/cube.png")
        self.lineWithCircles_icon = PhotoImage(file="icons/lineWithCircles.png")

        self.create_button(self.line_icon, lambda: (self.app.editor.set_tool(Line), self.app.show_popup("лінію")),
                           "Намалювати лінію")
        self.create_button(self.dot_icon, lambda: (self.app.editor.set_tool(Dot), self.app.show_popup("точку")),
                           "Намалювати точку")
        self.create_button(self.rectangle_icon,
                           lambda: (self.app.editor.set_tool(Rectangle), self.app.show_popup("прямокутник")),
                           "Намалювати прямокутник")
        self.create_button(self.elipse_icon, lambda: (self.app.editor.set_tool(Elipse), self.app.show_popup("еліпс")),
                           "Намалювати еліпс")
        self.create_button(self.lineWithCircles_icon, lambda: (
        self.app.editor.set_tool(LineWithCircles), self.app.show_popup("відрізок з колами")),
                           "Намалювати відрізок з колами")
        self.create_button(self.cube_icon, lambda: (self.app.editor.set_tool(Cube), self.app.show_popup("куб")),
                           "Намалювати куб")

    def create_button(self, image, command, tooltip_text):
        button = Button(self.toolbar_frame, image=image, command=command)
        button.image = image
        button.pack(side=tk.LEFT, padx=2, pady=2)
        self.create_tooltip(button, tooltip_text)

    @staticmethod
    def create_tooltip(widget, text):
        tooltip = Tooltip(widget, text)


class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        x = self.widget.winfo_rootx() + 40
        y = self.widget.winfo_rooty() + 40
        self.tooltip_window = Toplevel(self.widget)
        self.tooltip_window.wm_overrideredirect(True)
        self.tooltip_window.geometry(f"+{x}+{y}")
        label = tk.Label(self.tooltip_window, text=self.text, bg="white", relief=tk.SOLID, borderwidth=1)
        label.pack()

    def hide_tooltip(self, event=None):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None


class App:
    def __init__(self, root):
        self.start_x = None
        self.current_shape = None
        self.root = root
        self.root.title("Lab4")

        menu_bar = Menu(root)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open")
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
        MyEditor(self.canvas)
        self.editor = MyEditor.get_instance()
        self.editor.set_tool(Elipse)

    def show_popup(self, tool_name):
        popup = Toplevel(self.root)
        popup.wm_overrideredirect(True)
        popup.geometry(f"+{self.root.winfo_x() + 100}+{self.root.winfo_y() + 50}")
        label = tk.Label(popup, text=f"Обрано: {tool_name}", bg="lightyellow", relief=tk.SOLID, borderwidth=1)
        label.pack()

        self.root.after(1000, popup.destroy)
