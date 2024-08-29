from tkinter import Canvas, Tk, BOTH


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end


    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.start.x, self.start.y, 
            self.end.x, self.end.y, 
            fill=fill_color,
            width=2
        )


class Window:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.__root = Tk()
        self.__root.title("Maze Runner")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__running = False

    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.__canvas, fill_color)
