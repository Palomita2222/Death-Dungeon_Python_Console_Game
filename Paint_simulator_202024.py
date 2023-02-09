#import all modules required (keyboard for inputs, time for pause in the loop, os for cls, random for the block generation, and colorama for UI)
import keyboard
from time import sleep
import os
import random
from colorama import Fore as f

winbanner = f"""{f.GREEN}

 __   __  _______  __   __    _     _  ___   __    _  __  
|  | |  ||       ||  | |  |  | | _ | ||   | |  |  | ||  | 
|  |_|  ||   _   ||  | |  |  | || || ||   | |   |_| ||  | 
|       ||  | |  ||  |_|  |  |       ||   | |       ||  | 
|_     _||  |_|  ||       |  |       ||   | |  _    ||__| 
  |   |  |       ||       |  |   _   ||   | | | |   | __  
  |___|  |_______||_______|  |__| |__||___| |_|  |__||__| 

"""

#Create class for game
class Grid:

    def __init__(self ,width ,height):
        #Create variables used in functions and more...
        self.blocks = []
        self.inventory = 0
        self.last2x = 0
        self.last2y = 0
        self.width = width
        self.height = height
        self.grid = []
        self.placeableObjects = 0
        self.objectives = 0
        self.objectives_pos = []
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
                    #Random blocks spawn
                    key = random.randint(1,10)
                    key2 = random.randint(1,20)
                    if key == 10:
                        self.listax.append(2)
                        self.placeableObjects +=1
                    elif key2 == 20:
                        if self.placeableObjects > self.objectives:
                            self.listax.append(3)
                            self.objectives_pos.append([x_,y_])
                            self.objectives+=1
                    else:
                        self.listax.append(0)
                    
            self.grid.append(self.listax)
    #Function to show UI
    def show_grid(self):
        #Create a grid with UI sprites
        self.uigrid = []
        for row in self.grid:
            self.row = []
            for square in row:
                #Numbers in grid determine the block type
                if square == 0:
                    self.row.append("⬛")
                elif square == 1:
                    self.row.append("⬜")
                elif square == 2:
                    self.row.append("🟥")
                elif square == 3:
                    self.row.append("🟨")
            self.uigrid.append(self.row)
        #Code to generate and print what the player sees
        for row in self.uigrid:
            self.final = ""
            for box in row:
                self.final += box
            print(self.final)
    
    #Function used to move character
    def move(self,x,y):
        #No glitching through walls
        if len(self.grid) == y or len(self.grid[self.height-1]) == x or y == -1 or x == -1 or self.grid[y][x] == 3:
            pass
        else:
            #Delete player block where he was before, and draw him in the next coord
            self.grid[self.lasty][self.lastx] = 0
            self.player = [x,y]
            self.last2x = self.lastx
            self.last2y = self.lasty
            self.lastx = x
            self.lasty = y
            #if the block in front is a placeable block, then it will store it
            if self.grid[y][x] == 2:
                self.inventory+=1
            self.grid[y][x] = 1
    
    #Function used to place blocks
    def place(self,x,y):
        #Only place if blocks in inventory
        if self.inventory > 0:
            #Make sure no bugs happen when placing (placing on other blocks or placing them in the walls)
            if len(self.grid) == y or len(self.grid[self.height-1]) == x or y == -1 or x == -1 or self.grid[y][x] == 2:
                pass
            else:
                if self.grid[y][x] == 3:
                    self.objectives-=1
                #Store location of blocks (for purpuses not yet known)
                self.blocks.append([x,y])
                self.grid[y][x] = 2
                #subtract a block from the inventory
                self.inventory-=1

    


#Create game
hello = Grid(int(input("Grid width > ")),int(input("Grid height > ")))

#Game_loop
while True:
    hello.show_grid()
    print(f"{f.GREEN}Inventory : {f.BLUE}{hello.inventory} {f.GREEN}blocks")
    print(f"{f.GREEN}Objectives left : {f.BLUE}{hello.objectives}")
    if hello.objectives == 0:
        print(winbanner)
        sleep(5)
        break
    #if keyboard.wait("w") == True:
    #    hello.move(hello.lastx,hello.lasty+1)
    #check if a key is pressed, and move the character in that position
    if keyboard.is_pressed("w"):
        if hello.lasty != 0:
            hello.move(abs(hello.lastx),abs(hello.lasty)-1)
    if keyboard.is_pressed("s"):
        if hello.lasty != hello.height:
            hello.move(abs(hello.lastx),abs(hello.lasty)+1)
    if keyboard.is_pressed("a"):
        if hello.lastx != 0:
            hello.move(abs(hello.lastx)-1,abs(hello.lasty))
    if keyboard.is_pressed("d"):
        if hello.lastx != hello.width:
            hello.move(abs(hello.lastx)+1,abs(hello.lasty))
    if keyboard.is_pressed(" "):
        hello.place((hello.lastx - hello.last2x)+hello.lastx,(hello.lasty - hello.last2y)+hello.lasty)
    #Leave key
    if keyboard.is_pressed("l"):
        print(f"l key pressed! {f.RED}Leaving...{f.RESET}")
        sleep(3)
        os.system("cls")
        break
    #0.1 sec between updates, to prevent fast movement and also code crashing
    sleep(0.1)
    os.system("cls")
