from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.width = width
        self.height = height
        self.canvas = Canvas(self.__root)
        self.pack = self.canvas.pack()
        self.run = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()


    def wait_for_close(self):
        self.run = True
        while self.run:
            self.redraw()


    def close(self):
        self.run = False
