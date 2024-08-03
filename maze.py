from graphics import Window
from cell import Cell


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
       self.__x1 = x1
       self.__y1 = y1
       self.num_rows = num_rows
       self.num_cols = num_cols
       self.cell_size_x = cell_size_x
       self.cell_size_y = cell_size_y
