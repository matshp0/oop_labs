from abc import ABC, abstractmethod


class Editor(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def on_button_press(self, event):
        pass

    @abstractmethod
    def on_mouse_drag(self, event):
        pass

    @abstractmethod
    def on_button_release(self, event):
        pass
