from graphics import *

class Cell:
    def __init__(self, win: Window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None

        self._visited = False

        self._win = win


    def draw(self, x1: int, y1: int, x2: int, y2: int):
        if self._win is None:
            return

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "black")
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")

    def draw_move(self, other: 'Cell', undo=False):
        hlength = abs(self._x2 - self._x1) // 2
        x_center = hlength + self._x1
        y_center = hlength + self._y1

        hlength2 = abs(other._x2 - other._x1) // 2
        x_center2 = hlength2 + other._x1
        y_center2 = hlength2 + other._y1

        fill_color = "gray" if undo else "red"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._win.draw_line(line, fill_color)
