import tkinter as tk
import subprocess
import win32gui
import win32api
import win32con
import ctypes
import time

CUSTOM_MESSAGE_ID = win32con.WM_USER + 1


class Lab6Manager:
    def __init__(self, root):
        self.hwnd = self.create_message_window()
        self.object2_process = None
        self.object3_process = None
        self.root = root
        self.root.title("Lab6 Manager")
        self.set_window_position(20, 20)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        tk.Label(root, text="Enter matrix size (n):").grid(row=0, column=0, padx=10, pady=5)
        self.entry_n = tk.Entry(root)
        self.entry_n.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Enter Min value:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_min = tk.Entry(root)
        self.entry_min.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Enter Max value:").grid(row=2, column=0, padx=10, pady=5)
        self.entry_max = tk.Entry(root)
        self.entry_max.grid(row=2, column=1, padx=10, pady=5)

        launch_btn = tk.Button(root, text="Submit", command=self.on_submit_button)
        launch_btn.grid(row=3, column=0, columnspan=2, pady=5)

    def set_window_position(self, x_pos, y_pos):
        self.root.geometry(f"280x150+{x_pos}+{y_pos}")

    def on_submit_button(self):
        self.launch_object2()
        self.send_data_to_object2()

    def send_data_to_object2(self):
        try:
            n = int(self.entry_n.get())
            min_val = int(self.entry_min.get())
            max_val = int(self.entry_max.get())

            if n <= 0 or min_val > max_val:
                raise ValueError("Invalid input: Ensure n > 0 and min_val <= max_val")

            data = f"{n},{min_val},{max_val}"
            data_bytes = data.encode('utf-8')

            class COPYDATASTRUCT(ctypes.Structure):
                _fields_ = [
                    ("dwData", ctypes.c_void_p),
                    ("cbData", ctypes.c_size_t),
                    ("lpData", ctypes.c_void_p),
                ]

            copy_data_struct = COPYDATASTRUCT()
            copy_data_struct.dwData = 0
            copy_data_struct.cbData = len(data_bytes)
            copy_data_struct.lpData = ctypes.cast(
                ctypes.create_string_buffer(data_bytes), ctypes.c_void_p
            )

            hwnd = win32gui.FindWindow("Object2Class", None)
            if hwnd == 0:
                raise RuntimeError("Object2 window not found. Please ensure Object2 is running.")

            win32gui.SendMessage(
                hwnd,
                win32con.WM_COPYDATA,
                0,
                ctypes.addressof(copy_data_struct)
            )
            print(f"Sent data to Object2: {data}")

        except ValueError as e:
            tk.messagebox.showerror("Input Error", f"Invalid input: {e}")
        except RuntimeError as e:
            tk.messagebox.showerror("Runtime Error", str(e))

    def create_message_window(self):
        wnd_class = win32gui.WNDCLASS()
        wnd_class.hInstance = win32api.GetModuleHandle(None)
        wnd_class.lpszClassName = "Object1Class"
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
        if msg == CUSTOM_MESSAGE_ID:
            self.launch_object3()
            self.send_data_to_object3()
        return win32gui.DefWindowProc(hwnd, msg, wparam, lparam)

    def send_data_to_object3(self):
        def enum_window_callback(hwnd, lparam):
            if win32gui.GetClassName(hwnd) == "Object3Class":
                win32api.SendMessage(hwnd, CUSTOM_MESSAGE_ID, 0, 0)

        win32gui.EnumWindows(enum_window_callback, None)

    def launch_object2(self):
        hwnd = win32gui.FindWindow("Object2Class", None)
        if not hwnd:
            self.object2_process = subprocess.Popen(["python", "Object2.py"])
            time.sleep(0.2)

    def launch_object3(self):
        hwnd = win32gui.FindWindow("Object3Class", None)
        print("trying to launch")
        if not hwnd:
            self.object3_process = subprocess.Popen(["python", "Object3.py"])

    def on_close(self):
        if self.object2_process and self.object2_process.poll() is None:
            self.object2_process.terminate()
        if self.object3_process and self.object3_process.poll() is None:
            self.object3_process.terminate()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = Lab6Manager(root)
    root.mainloop()
