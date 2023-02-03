import keyboard
from time import sleep
import os


class Grid:

    def __init__(self ,width ,height):
        self.blocks = []
        self.width = width
        self.height = height
        self.grid = []
        self.playercounter = 0
        for y_ in range(height):
            self.listax = []
            for x_ in range(width):
                if self.playercounter == 0:
                    self.player = [0,0]
                    self.listax.append(1)
                    self.lastx = 0
                    self.lasty = 0
                    self.playercounter +=1
                else:
                    self.listax.append(0)
            self.grid.append(self.listax)
                
    
    def show_grid(self):
        self.uigrid = []
        self.final = ""
        for row in self.grid:
            self.row = []
            for square in row:
                if square == 0:
                    self.row.append("⬛")
                elif square == 1:
                    self.row.append("⬜")
                elif square == 2:
                    self.row.append("🔴")
            self.uigrid.append(self.row)
        for row in self.uigrid:
            self.final = ""
            for box in row:
                self.final += box
            print(self.final)
    
    def move(self,x,y):
        self.grid[self.lasty][self.lastx] = 0
        self.player = [x,y]
        self.lastx = x
        self.lasty = y
        self.grid[y][x] = 1
    
    def place(self,x,y):
        #Store location of blocks (for purpuses unknown)
        self.blocks.append([x,y])
        self.grid[y][x] = 2



hello = Grid(int(input("Grid width > ")),int(input("Grid height > ")))


while True:
    hello.show_grid()
    #if keyboard.wait("w") == True:
    #    hello.move(hello.lastx,hello.lasty+1)
    if keyboard.is_pressed("w"):
        if hello.lasty != 0:
            hello.move(abs(hello.lastx),abs(hello.lasty)-1)
    if keyboard.is_pressed("s"):
        if hello.lasty != hello.height:
            hello.move(abs(hello.lastx),abs(hello.lasty)+1)
    if keyboard.is_pressed("a"):
        if hello.lasty != 0:
            hello.move(abs(hello.lastx)-1,abs(hello.lasty))
    if keyboard.is_pressed("d"):
        if hello.lastx != hello.width:
            hello.move(abs(hello.lastx)+1,abs(hello.lasty))
    if keyboard.is_pressed(" "):
        hello.place(hello.lastx+1,hello.lasty)
    sleep(0.1)
    os.system("cls")