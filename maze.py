import random

from time import sleep
from typing import List

from cell import Cell
from graphics import Window


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window=None,
        seed: int=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed:
            random.seed(seed)

        self._cells: List[List[Cell]] = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    
    def solve(self) -> bool:
        return self._solve_r(0, 0)

    def _solve_r(self, i, j) -> bool:
        self._animate()
        self._cells[i][j]._visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        if i > 0 and not self._cells[i][j].has_left_wall and not self._cells[i - 1][j]._visited:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i - 1][j], undo=True)

        if j > 0 and not self._cells[i][j].has_top_wall and not self._cells[i][j - 1]._visited:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j - 1], undo=True)

        if i < self._num_cols - 1 and not self._cells[i][j].has_right_wall and not self._cells[i + 1][j]._visited:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i + 1][j], undo=True)

        if j < self._num_rows - 1 and not self._cells[i][j].has_bottom_wall and not self._cells[i][j + 1]._visited:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j + 1], undo=True)
        
        return False

    def _create_cells(self) -> None:
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int) -> None:
        if self._win is None:
            return
        
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _break_entrance_and_exit(self) -> None:
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j) -> None:
        self._cells[i][j]._visited = True
        while True:
            to_visit = []
            if i > 0 and not self._cells[i - 1][j]._visited:
                to_visit.append((i - 1, j))
            if j > 0 and not self._cells[i][j - 1]._visited:
                to_visit.append((i, j - 1))
            if i < self._num_cols - 1 and not self._cells[i + 1][j]._visited:
                to_visit.append((i + 1, j))
            if j < self._num_rows - 1 and not self._cells[i][j + 1]._visited:
                to_visit.append((i, j + 1))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            direction = random.randrange(len(to_visit))
            next_idx = to_visit[direction]
            
            if next_idx[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[next_idx[0]][next_idx[1]].has_right_wall = False
            if next_idx[0] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[next_idx[0]][next_idx[1]].has_bottom_wall = False
            if next_idx[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[next_idx[0]][next_idx[1]].has_left_wall = False
            if next_idx[0] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_idx[0]][next_idx[1]].has_top_wall = False

            self._break_walls_r(next_idx[0], next_idx[1])

    def _reset_cells_visited(self) -> None:
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j]._visited = False

    def _animate(self) -> None:
        if self._win is None:
            return

        self._win.redraw()
        sleep(0.05) 