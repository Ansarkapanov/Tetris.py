from Tkinter import *
import random


class Game: 
    CANVAS_WIDTH = 450
    CANVAS_HEIGHT = 600 
    BOX_SIZE = 30 

    def __init__(self):
        Game.root = Tk()
        self.canvas = Canvas(Game.root, width = Game.CANVAS_WIDTH, height = Game.CANVAS_HEIGHT)
        self.canvas.config(bg="white")
        self.canvas.pack()

        random.seed()
        
        # initialize grid
        self.grid = Grid()
        self.grid.draw(self.canvas)

        self.shape = Shape()
        self.shape.draw(self.canvas)

        self.timer()

        Game.root.bind("<Key>", self.handle_keyboard_input)

        Game.root.mainloop()

    def timer(self):
        self.grid.draw(self.canvas)
        self.shape.lower()
        self.shape.draw(self.canvas)

        Game.root.after(500, self.timer)

    def handle_keyboard_input(self, event):
        self.grid.draw(self.canvas)
        self.shape.draw(self.canvas)
        if event.keysym == "Up": self.shape.rotate()
        elif event.keysym == "Left": self.shape.moveLeft()
        elif event.keysym == "Right": self.shape.moveRight()
        else: print event.keysym

class Grid: 
    ROW_COUNT = Game.CANVAS_WIDTH / Game.BOX_SIZE
    COL_COUNT = Game.CANVAS_HEIGHT / Game.BOX_SIZE

    def __init__(self):
        self.arr = [[0 for i in range(Grid.ROW_COUNT)] for j in range(Grid.COL_COUNT)]
        print "Grid initialized"

    def draw(self, canvas):

        for i in range(Grid.COL_COUNT):
            for j in range(Grid.COL_COUNT):
                x = i * Game.BOX_SIZE
                y = j * Game.BOX_SIZE
                canvas.create_rectangle(x, y, x + Game.BOX_SIZE, y + Game.BOX_SIZE, fill="white")


class Shape:
    S = [[0,-1], [0,0], [1,0], [1,1]]
    Z = [[0,1], [0,0], [-1,0], [-1,1]]
    I = [[0,-2], [0,-1], [0,1], [0,2]]
    T = [[-1,0], [0,-1], [1,0]]
    O = [[-1,0], [-1,1], [0,-1]]
    L1 = [[-1,0], [0,0], [1,0], [1,1]]
    L2 = [[-1,0], [0,0], [1,0], [-1,1]]

    SHAPES = [S, Z, I, T, O, L1, L2]
    CENTER = [2,2]
    GRID_SIZE = 5

    def __init__(self):
        self.grid = [[0 for i in range(Shape.GRID_SIZE)] for j in range(Shape.GRID_SIZE)]
        self.x = round(Grid.ROW_COUNT / 2) * Game.BOX_SIZE
        self.y = -1 * Game.BOX_SIZE
        self.current_shape = Shape.S

    def draw(self, canvas):
        for i in range(len(self.current_shape)):
            self.grid[self.current_shape[i][0] + Shape.CENTER[0]][self.current_shape[i][1] + Shape.CENTER[1]] = 1 
            
        for i in range(Shape.GRID_SIZE):
            for j in range(Shape.GRID_SIZE):
                temp_x = self.x + i * Game.BOX_SIZE
                temp_y = self.y + j * Game.BOX_SIZE
                if self.grid[i][j]: canvas.create_rectangle(temp_x, temp_y, temp_x + Game.BOX_SIZE, temp_y + Game.BOX_SIZE, fill="black") 

    def lower(self):
        self.y += Game.BOX_SIZE

    def rotate(self): 
        for i in range(len(self.current_shape)): 
            self.grid[self.current_shape[i][0] + Shape.CENTER[0]][self.current_shape[i][1] + Shape.CENTER[1]] = 0

            rel_x_coord = self.current_shape[i][0]
            rel_y_coord = self.current_shape[i][1]

            self.current_shape[i][0] = rel_y_coord
            self.current_shape[i][1] = -rel_x_coord

    def moveLeft(self):
        self.x -= Game.BOX_SIZE

    def moveRight(self):
        self.x += Game.BOX_SIZE

if __name__ == "__main__": 
    game = Game()
