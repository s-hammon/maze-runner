import sys

from graphics import Window
from maze import Maze

def main():
    num_rows = 9
    num_cols = 12
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10**3)

    win = Window(screen_x, screen_y)
    maze = Maze(
        margin, margin, 
        num_rows, num_cols, 
        cell_size_x, cell_size_y,
        win,
        # 404
    )
    maze._break_entrance_and_exit()
    maze.solve()

    win.wait_for_close()

main()