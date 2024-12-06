import tkinter as tk
from tkinter import Menu, Toplevel, filedialog
from shapes import Elipse, Rectangle, Line, Dot, LineWithCircles, Cube
from MyTable import MyTable
from hepers.ObservableList import ObservableList
from MyEditor import MyEditor
from hepers.Toolbar import Toolbar

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
        file_menu.add_command(label="Open", command=self.load)
        file_menu.add_command(label="Save", command=self.save)
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

        table_menu = Menu(menu_bar, tearoff=0)
        table_menu.add_command(label="Показати", command=self.open_table)
        table_menu.add_command(label="Сховати", command=self.close_table)
        menu_bar.add_cascade(label="Таблиця елементів", menu=table_menu)

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

    def save(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if not file_path:
            return

        with open(file_path, 'w') as file:
            for el in self.shapes:
                shape = el.__class__.__name__
                x1, y1, x2, y2 = el.x1, el.y1, el.x2, el.y2
                file.write(f"{shape}\t{x1}\t{y1}\t{x2}\t{y2}\n")

        print(f"Shapes saved to {file_path}")

    def load(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if not file_path:
            return

        with open(file_path, 'r') as file:
            self.editor.clear_all_shapes()
            for line in file:
                data = line.strip().split("\t")
                if len(data) == 5:
                    shape, x1, y1, x2, y2 = data
                    x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))
                    tool = globals()[shape]
                    self.editor.draw_by_coordinates(tool, x1, y1, x2, y2)
                    print(shape, x1, y1, x2, y2)

        print(f"Shapes loaded from {file_path}")

