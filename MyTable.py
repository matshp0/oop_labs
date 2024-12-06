import tkinter as tk
from tkinter import ttk


class MyTable:
    instance = None  # Singleton instance

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

        # Create a custom font with larger size
        font = ('Arial', 12)  # Change the font size here (14 is bigger)

        self.tree = ttk.Treeview(frame, columns=columns, show="headings", style="Custom.Treeview")

        # Define column headings with custom font
        for col in columns:
            self.tree.heading(col, text=col, anchor=tk.CENTER)
            self.tree.column(col, width=80, anchor=tk.CENTER)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Adding vertical scrollbar
        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Set the font for the entire treeview (including rows)
        style = ttk.Style()
        style.configure("Custom.Treeview", font=font)

        # Draw initial data
        self.redraw_table()

    def redraw_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for index, el in enumerate(self.shapes):
            shape = el.__class__.__name__
            x1, y1, x2, y2 = el.x1, el.y1, el.x2, el.y2
            self.tree.insert("", tk.END, values=(shape, x1, y1, x2, y2), iid=index)

    def on_add(self, index):
        """Handler for 'add' event in shapes."""
        print("Added new shape", index, self.shapes[index].__class__.__name__)
        self.redraw_table()  # Redraw the table instead of creating a new one

    def on_delete(self, event):
        """Handler for DELETE key press."""
        selected_item = self.tree.selection()  # Get the selected item
        if not selected_item:
            return  # No item selected

        # Get the index of the selected row
        selected_item_id = selected_item[0]
        index = self.tree.index(selected_item_id)  # Get the index of the selected item
        self.shapes.remove(index)

        # Redraw the table after removal
        self.redraw_table()

    def show_window(self):
        self.window.deiconify()
        self.window.lift()

    def hide_window(self):
        self.window.withdraw()

    def close(self):
        self.window.destroy()
        MyTable.instance = None
