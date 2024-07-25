from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.widget = Tk()
        self.title = self.widget.title()


    def redraw(self):
        ...


    def wait_for_close(self):
        ...


    def close(self):
        ...


def main():
    ...


if __name__ == '__main__':
    main()
