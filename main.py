from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.title = self.__root.title()
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


def main():
    win = Window(800, 600)
    win.wait_for_close()


if __name__ == '__main__':
    main()
