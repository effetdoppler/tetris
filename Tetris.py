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
        self.block = Block(self, self.can)

    def grid(self):
        gap = 0
        for i in range(10):
            gap += 20
            self.can.create_line(gap, 0, gap, self.height, fill="green")
        gap = 0
        for i in range(20):
            gap += 20
            self.can.create_line(0, gap, self.width, gap, fill="green")


class Block(object):
    def __init__(self, app, can):
        self.can = can
        self.app = app
        self.size = 20
        self.spawn()

    def spawn(self):
        self.body = self.can.create_rectangle(self.app.width/2, 0, self.app.width/2+20, 20, fill="red")



if __name__ == '__main__':
    Application(200, 400).mainloop()
