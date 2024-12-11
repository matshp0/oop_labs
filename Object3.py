import tkinter as tk
import win32gui
import win32con
import win32api
import numpy as np


class Object3:
    def __init__(self, root):
        self.hwnd = self.create_message_window()
        self.root = root
        self.root.title("Object3 - Determinant Calculator")
        self.root.geometry("400x300+700+200")
        self.text_box = tk.Text(self.root, width=40, height=10)
        self.text_box.pack(padx=10, pady=10)

        self.display_determinant()

    def read_from_clipboard(self):
        clipboard_content = self.root.clipboard_get()
        try:
            matrix = [list(map(int, row.split())) for row in clipboard_content.strip().split('\n')]
            return matrix
        except ValueError:
            return None

    def create_message_window(self):
        wnd_class = win32gui.WNDCLASS()
        wnd_class.hInstance = win32api.GetModuleHandle(None)
        wnd_class.lpszClassName = "Object3Class"
        wnd_class.lpfnWndProc = self.window_proc
        wnd_class_atom = win32gui.RegisterClass(wnd_class)

        hwnd = win32gui.CreateWindow(
            wnd_class_atom,
            "Object3 - Determinant Calculator",
            win32con.WS_OVERLAPPEDWINDOW,
            100, 100, 400, 300,
            0, 0, wnd_class.hInstance, None
        )
        return hwnd

    def window_proc(self, hwnd, msg, wparam, lparam):
        if msg == win32con.WM_USER + 1:
            self.handle_custom_message()
        return win32gui.DefWindowProc(hwnd, msg, wparam, lparam)

    def handle_custom_message(self):
        print("Custom message received, recalculating determinant.")
        self.display_determinant()

    def calculate_determinant(self, matrix):
        return round(np.linalg.det(np.array(matrix)), 2)

    def display_determinant(self):
        matrix = self.read_from_clipboard()
        self.text_box.delete(1.0, tk.END)

        if matrix is None:
            self.text_box.insert(tk.END, "Error: Invalid or missing matrix in clipboard.\n")
            return

        try:
            determinant = self.calculate_determinant(matrix)
            self.text_box.insert(tk.END, "Matrix Determinant:\n")
            self.text_box.insert(tk.END, f"{determinant}\n")
        except Exception as e:
            self.text_box.insert(tk.END, f"Error calculating determinant: {e}\n")

    def send_custom_message(self):
        win32api.SendMessage(self.hwnd, win32con.WM_USER + 1, 0, 0)
        print("Custom message sent to the window.")


if __name__ == "__main__":
    root = tk.Tk()
    app = Object3(root)

    app.send_custom_message()
    root.mainloop()
