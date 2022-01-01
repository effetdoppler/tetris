from tkinter import *


class Application(Frame):
    def __init__(self, x, y):
        Frame.__init__(self)
        self.pack()
        self.width = x
        self.height = y
        self.can = Canvas(self, width=self.width, height=self.height, bg='black', relief=SUNKEN)
        self.can.pack()
        self.grid()

    def grid(self):
        gap = 0
        for i in range(10):
            gap += 20
            self.can.create_line(gap, 0, gap, self.height, fill="green")
        gap = 0
        for i in range(20):
            gap += 20
            self.can.create_line(0, gap, self.width, gap, fill="green")



if __name__ == '__main__':
    Application(200, 400).mainloop()
