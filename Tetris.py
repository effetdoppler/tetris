from tkinter import *


class Application(Frame):
    def __init__(self, x, y):
        Frame.__init__(self)
        self.pack()
        self.width = x
        self.height = y
        self.state = []
        self.can = Canvas(self, width=self.width, height=self.height, bg='black', relief=SUNKEN)
        self.can.pack()
        self.frame = Frame(self)
        self.startbutton = Button(self.frame, text="commencer", command=self.start)
        self.startbutton.pack(side=LEFT)
        self.destroybutton = Button(self.frame, text="quitter", command=self.quit)
        self.destroybutton.pack(side=RIGHT)
        self.frame.pack()
        self.grid()

    def initstate(self):
        for i in range(40):
            self.state.append(20*[0])

    def grid(self):
        gap = 0
        for i in range(10):
            gap += 20
            self.can.create_line(gap, 0, gap, self.height, fill="green")
        gap = 0
        for i in range(20):
            gap += 20
            self.can.create_line(0, gap, self.width, gap, fill="green")

    def start(self):
        self.initstate()
        self.block = Block(self, self.can, self.state)


class Block(object):
    def __init__(self, app, can, state):
        self.can = can
        self.app = app
        self.state = state
        self.size = 20
        self.pos = [0, 10]
        self.spawn()

    def spawn(self):
        self.state[self.pos[0]][self.pos[1]] = 1
        self.body = self.can.create_rectangle(self.pos[1]*10, self.pos[0]*10, self.pos[1]*10+20, self.pos[0]*10+20, fill="red")


if __name__ == '__main__':
    Application(200, 400).mainloop()
