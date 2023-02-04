import keyboard
from time import sleep
import os

#Create class for game
class Grid:

    def __init__(self ,width ,height):
        #Create variables used in functions and more...
        self.blocks = []
        self.last2x = 0
        self.last2y = 0
        self.width = width
        self.height = height
        self.grid = []
        self.playercounter = 0
        #Create grid
        for y_ in range(height):
            self.listax = []
            for x_ in range(width):
                #add player
                if self.playercounter == 0:
                    self.player = [0,0]
                    self.listax.append(1)
                    self.lastx = 0
                    self.lasty = 0
                    self.playercounter +=1
                else:
                    self.listax.append(0)
            self.grid.append(self.listax)
                
    #Function to show UI
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
    
    #Function used to move character
    def move(self,x,y):
        #No glitching through walls
        if len(self.grid) == y or len(self.grid[self.height-1]) == x or y == -1 or x == -1:
            pass
        else:
            self.grid[self.lasty][self.lastx] = 0
            self.player = [x,y]
            self.last2x = self.lastx
            self.last2y = self.lasty
            self.lastx = x
            self.lasty = y
            self.grid[y][x] = 1
    
    #Function used to place blocks
    def place(self,x,y):
        if len(self.grid) == y or len(self.grid[self.height-1]) == x or y == -1 or x == -1:
            pass
        else:
            #Store location of blocks (for purpuses not yet known)
            self.blocks.append([x,y])
            self.grid[y][x] = 2

    """
    def carry_block(self,x,y):
        coming soon!
    """
    


#Create game
hello = Grid(int(input("Grid width > ")),int(input("Grid height > ")))

#Game_loop
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
        hello.place((hello.lastx - hello.last2x)+hello.lastx,(hello.lasty - hello.last2y)+hello.lasty)
    if keyboard.is_pressed("l"):
        break
    sleep(0.1)
    os.system("cls")
print("l key pressed! Leaving...")
sleep(3)
os.system("cls")