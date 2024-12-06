import tkinter as tk
from tkinter import ttk


class MyTable:
    instance = None

    def __new__(cls, parent, shapes):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, parent, shapes):
        if hasattr(self, '_initialized') and self._initialized:
            self.show_window()
            return

        self._initialized = True
        self.parent = parent
        self.shapes = shapes
        self.shapes.on('add', self.on_add)
        self.window = tk.Toplevel(parent)
        self.window.title("Shapes Table")
        self.window.geometry("900x600")
        self.window.transient(parent)
        self.window.protocol("WM_DELETE_WINDOW", self.hide_window)

        self.create_table()
        self.window.withdraw()

        self.window.bind("<Delete>", self.on_delete)

    def create_table(self):
        frame = tk.Frame(self.window)
        frame.pack(fill=tk.BOTH, expand=True)

        columns = ("Shape", "x1", "y1", "x2", "y2")

        font = ('Arial', 12)

        self.tree = ttk.Treeview(frame, columns=columns, show="headings", style="Custom.Treeview")

        for col in columns:
            self.tree.heading(col, text=col, anchor=tk.CENTER)
            self.tree.column(col, width=80, anchor=tk.CENTER)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        style = ttk.Style()
        style.configure("Custom.Treeview", font=font)

        self.redraw_table()
        self.tree.bind("<<TreeviewSelect>>", self.on_item_selected)

    def redraw_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for index, el in enumerate(self.shapes):
            shape = el.__class__.__name__
            x1, y1, x2, y2 = el.x1, el.y1, el.x2, el.y2
            self.tree.insert("", tk.END, values=(shape, x1, y1, x2, y2), iid=index)

    def on_add(self, index):
        print("Added new shape", index, self.shapes[index].__class__.__name__)
        self.redraw_table()

    def on_delete(self, event):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        selected_item_id = selected_item[0]
        index = self.tree.index(selected_item_id)
        self.shapes.remove(index)

        self.redraw_table()

    def on_item_selected(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            selected_item_id = selected_item[0]
            index = self.tree.index(selected_item_id)
            self.shapes.emit('select', index)
            print(f"Selected item index: {index}")
            print(f"Selected item values: {self.tree.item(selected_item_id)['values']}")


    def show_window(self):
        self.window.deiconify()
        self.window.lift()

    def hide_window(self):
        self.window.withdraw()

    def close(self):
        self.window.destroy()
        MyTable.instance = None
