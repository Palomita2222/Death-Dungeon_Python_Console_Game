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
        self.last2x = 0
        self.last2y = 0
        self.width = width
        self.height = height
        self.grid = []
        self.playercounter = 0
        self.dirx = 0
        self.diry = 0
        #Create grid
        for y_ in range(height):
            self.listax = []
            for x_ in range(width):
                #add player
                if self.playercounter == 0:
                    self.player = [0,0]
                    self.listax.append(4)
                    self.lastx = 0
                    self.lasty = 0
                    self.playercounter +=1
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
                    self.row.append("⬛")#Nothing
                elif square == 1:
                    self.row.append("🟫")#Walls ⬜
                elif square == 2:
                    self.row.append("🟥")#Shop
                elif square == 3:
                    self.row.append("🟨")#Coins
                elif square == 4:
                    self.row.append("🟪")#Player
                elif square == 5:
                    self.row.append("🟩")#Zombie
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
        if len(self.grid) == y or len(self.grid[self.height-1]) == x or y == -1 or x == -1:
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
            self.grid[y][x] = 4
    
    #Function used to place blocks
    def place(self,x,y,b):
        if len(self.grid) == y or len(self.grid[self.height-1]) == x or y == -1 or x == -1:
            pass
        else:
            self.grid[y][x] = b


#Create game
hello = Grid(int(input("Grid width > ")),int(input("Grid height > ")))

#Game_loop
while True:
    hello.show_grid()
    print(f"1 for {f.BLACK} BLACK{f.RESET}, 2 for BROWN/Walls, 3 for {f.RED}RED/SHOP{f.RESET}, 4 for {f.YELLOW}YELLOW/COINS{f.RESET}, 5 for {f.GREEN}GREEN/TELEPORTER{f.RESET}.")
    print(f"Use {f.BLUE}arrows{f.RESET} to point to where you wanna place blocks.")
    print(f"PRESS 9 to generate {f.GREEN}map code{f.RESET}")
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
    if keyboard.is_pressed("right arrow"):
        hello.dirx = 1
    if keyboard.is_pressed("left arrow"):
        hello.dirx = -1
    if keyboard.is_pressed("up arrow"):
        hello.diry = -1
    if keyboard.is_pressed("down arrow"):
        hello.diry = 1
    if keyboard.is_pressed("right arrow") == False and keyboard.is_pressed("left arrow") == False:
        hello.dirx = 0
    if keyboard.is_pressed("up arrow") == False and keyboard.is_pressed("down arrow") == False:
        hello.diry = 0
    if keyboard.is_pressed("1"):
        hello.place(abs(hello.lastx+hello.dirx),abs(hello.lasty+hello.diry),0)#Black/Nothing
    if keyboard.is_pressed("2"):
        hello.place(abs(hello.lastx+hello.dirx),abs(hello.lasty+hello.diry),1)#Brown/Wallls
    if keyboard.is_pressed("3"):
        hello.place(abs(hello.lastx+hello.dirx),abs(hello.lasty+hello.diry),2)#Shop
    if keyboard.is_pressed("4"):
        hello.place(abs(hello.lastx+hello.dirx),abs(hello.lasty+hello.diry),3)#Coins
    if keyboard.is_pressed("5"):
        hello.place(abs(hello.lastx+hello.dirx),abs(hello.lasty+hello.diry),5)#TP
    if keyboard.is_pressed("9"):
        print(hello.grid)
        break
    if keyboard.is_pressed("l"):
        print(f"l key pressed! {f.RED}Leaving...{f.RESET}")
        sleep(3)
        os.system("cls")
        break
    #0.1 sec between updates, to prevent fast movement and also code crashing
    sleep(0.1)
    os.system("cls")
