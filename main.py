from tkinter import Tk, BOTH, Canvas


def main():
    win = Window(800, 600)
    win.wait_for_close()


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.__root = Tk()
        self.__root.title("Maze Runner")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas()
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
        
if __name__ == "__main__":
    main()