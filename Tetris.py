from tkinter import *


class Application(Frame):
    def __init__(self, x, y):
        Frame.__init__(self)
        self.pack()
        self.width = x
        self.height = y
        self.can = Canvas(self, width=self.width, height=self.height, bg='ivory', bd=3, relief=SUNKEN)
        self.can.pack()


if __name__ == '__main__':
    Application(300, 400).mainloop()
