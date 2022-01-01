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
        for i in range(20): #row
            self.state.append(10*[0]) #column

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
        #self.initstate()
        self.block = Block(self, self.can)
        self.block.fall()


class Block(object):
    def __init__(self, app, can):
        self.can = can
        self.app = app
        #self.state = state
        self.size = 20
        self.alive = True
        self.pos = [0, 5] #[row, column]
        self.body = None
        self.spawn()

    def spawn(self):
        #self.state[self.pos[0]][self.pos[1]] = 1
        self.body = self.can.create_rectangle(self.pos[1]*20, self.pos[0]*20, self.pos[1]*20+self.size, self.pos[0]*20+self.size, fill="red")

    def move(self):
        self.can.coords(self.body, self.pos[1]*20, self.pos[0]*20, self.pos[1]*20+self.size, self.pos[0]*20+self.size)

    def fall(self):
        if self.pos[0] < 19:
            self.pos[0] += 1
            self.move()
            self.app.after(200, self.fall)
        else:
            self.alive = False


if __name__ == '__main__':
    Application(200, 400).mainloop()
