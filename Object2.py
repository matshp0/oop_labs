import tkinter as tk
from tkinter import messagebox
import win32gui
import win32con
import win32api
import ctypes
import numpy as np

CUSTOM_MESSAGE_ID = win32con.WM_USER + 1


class Object2:
    class COPYDATASTRUCT(ctypes.Structure):
        _fields_ = [
            ("dwData", ctypes.c_void_p),
            ("cbData", ctypes.c_size_t),
            ("lpData", ctypes.c_void_p),
        ]

    def __init__(self, root, x_pos=100, y_pos=100):
        self.root = root
        self.root.title("Object2 - Matrix Generator")

        self.set_window_position(x_pos, y_pos)

        self.text_box = tk.Text(root, width=50, height=15)
        self.text_box.pack(padx=10, pady=10)

        self.generated_matrix = None

        self.hwnd = self.create_message_window()

    def set_window_position(self, x_pos, y_pos):
        self.root.geometry(f"400x300+{x_pos}+{y_pos}")

    def create_message_window(self):
        wnd_class = win32gui.WNDCLASS()
        wnd_class.hInstance = win32api.GetModuleHandle(None)
        wnd_class.lpszClassName = "Object2Class"
        wnd_class.lpfnWndProc = self.window_proc
        wnd_class_atom = win32gui.RegisterClass(wnd_class)

        hwnd = win32gui.CreateWindow(
            wnd_class_atom,
            "Object2 - Matrix Generator",
            win32con.WS_OVERLAPPEDWINDOW,
            100, 100, 400, 300,
            0, 0, wnd_class.hInstance, None
        )
        return hwnd

    def window_proc(self, hwnd, msg, wparam, lparam):
        if msg == win32con.WM_COPYDATA:
            self.wm_copydata_handler(hwnd, msg, wparam, lparam)
        return win32gui.DefWindowProc(hwnd, msg, wparam, lparam)

    def wm_copydata_handler(self, hwnd, msg, wparam, lparam):
        cds = ctypes.cast(lparam, ctypes.POINTER(self.COPYDATASTRUCT)).contents
        data_length = cds.cbData
        data_ptr = cds.lpData

        data = ctypes.string_at(data_ptr, data_length)
        params = data.decode("utf-8").split(",")

        try:
            n, min_val, max_val = map(int, params)
            self.generated_matrix = self.generate_matrix(n, min_val, max_val)

            self.text_box.delete(1.0, tk.END)
            self.text_box.insert(tk.END, f"Received parameters: n={n}, min={min_val}, max={max_val}\n")
            self.text_box.insert(tk.END, f"Generated {n}x{n} Matrix:\n")
            for row in self.generated_matrix:
                self.text_box.insert(tk.END, f"{row}\n")

            self.copy_to_clipboard()

        except Exception as e:
            messagebox.showerror("Error", f"Invalid data received: {e}")

    def copy_to_clipboard(self):
        if self.generated_matrix is None:
            return
        matrix_str = "\n".join(" ".join(map(str, row)) for row in self.generated_matrix)

        self.root.clipboard_clear()
        self.root.clipboard_append(matrix_str)
        self.root.update()
        self.send_custom_message_to_window()
        print("Matrix copied to clipboard!")

    def send_custom_message_to_window(self):
        def enum_window_callback(hwnd, lparam):
            if win32gui.GetClassName(hwnd) == "Object1Class":
                win32api.SendMessage(hwnd, CUSTOM_MESSAGE_ID, 0, 0)
                print(f"Custom message sent to window with HWND {hwnd} and class name Object1Class")

        win32gui.EnumWindows(enum_window_callback, None)

    @staticmethod
    def generate_matrix(n, min_val, max_val):
        return np.random.randint(min_val, max_val + 1, size=(n, n))


if __name__ == "__main__":
    root = tk.Tk()

    x_position = 200
    y_position = 200

    app = Object2(root, x_pos=x_position, y_pos=y_position)
    root.mainloop()
