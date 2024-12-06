import tkinter as tk
from shapes import Elipse, Rectangle, Line, Dot, LineWithCircles, Cube
from tkinter import Menu, Button, Toplevel, PhotoImage
from Tooltip import Tooltip


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
        self.create_button(self.lineWithCircles_icon, lambda: (self.app.editor.set_tool(LineWithCircles), self.app.show_popup("відрізок з колами")),
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
