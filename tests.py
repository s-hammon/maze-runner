import unittest

from maze import Maze


class Tests(unittest.TestCase):
    num_cols = 12
    num_rows = 10

    def test_maze_create_cells(self):
        m1 = Maze(0, 0, self.num_rows, self.num_cols, 10, 10, None, 404)
        self.assertEqual(
            len(m1._cells), self.num_cols
        )
        self.assertEqual(
            len(m1._cells[0]), self.num_rows
        )

    def test_maze_break_entrance_and_exit(self):
        m1 = Maze(0, 0, self.num_rows, self.num_cols, 10, 10, None, 404)
        self.assertEqual(
            m1._cells[0][0].has_top_wall, False
        )
        self.assertEqual(
            m1._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall, False
        )

    def test_maze_reset_cells_visited(self):
        m1 = Maze(0, 0, self.num_rows, self.num_cols, 10, 10, None, 404)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(cell._visited, False)

if __name__ == "__main__":
    unittest.main()