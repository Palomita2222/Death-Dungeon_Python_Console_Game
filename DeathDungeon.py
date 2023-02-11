#import all modules required (keyboard for inputs, time for pause in the loop, os for cls, random for the block generation, and colorama for UI)
import keyboard
from time import sleep
import os
import random
from colorama import Fore as f
import ast

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
class Game:

    def __init__(self,level):
        #Load game, variables...
        self.levels = [[[4, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 5, 0, 0, 0, 1, 0, 3, 0], [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 3, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1, 1], [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]],[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 5, 1, 1, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 5, 3, 3, 3, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]]]
        if level != "x":
            self.levels = ast.literal_eval(level)
            #For testing purposes
            """
            print(self.levels)
            print(type(self.levels))
            print(type(level))
            """
            self.grid = self.levels
        self.inventory = []
        self.coins = 0
        self.lastx = 0
        self.lasty = 0
        self.last2x = 0
        self.last2y = 0
        self.level = 0
        #If LOAD == FALSE, Then play normal maps
        if level == "x":
            self.grid = self.levels[self.level]
        print(self.grid)
        sleep(5)
        self.playercounter = 0
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        
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
                    self.row.append("🟫")#Walls
                elif square == 2:
                    self.row.append("🟥")#Shop
                elif square == 3:
                    self.row.append("🟨")#Coins
                elif square == 4:
                    self.row.append("🟪")#Player
                elif square == 5:
                    self.row.append("🟩")#Teleporter
            self.uigrid.append(self.row)
        #Code to generate and print what the player sees
        for row in self.uigrid:
            self.final = ""
            for box in row:
                self.final += box
            print(self.final)

    def teleport(self):
        #Teleporting function (only if next map availiable)
        if len(self.levels) > 1 and len(self.levels) > self.level:
            self.grid = self.levels[self.level]
            self.show_grid()
    
    #Function used to move character
    def move(self,x,y):
        #No glitching through walls
        if len(self.grid) == y or len(self.grid[self.height-1]) == x or y == -1 or x == -1 or self.grid[y][x] == 1 or self.grid[y][x] == 2:
            pass
        else:
            #Delete player block where he was before, and draw him in the next coord
            self.grid[self.lasty][self.lastx] = 0
            self.player = [x,y]
            self.last2x = self.lastx
            self.last2y = self.lasty
            self.lastx = x
            self.lasty = y
            if self.grid[y][x] == 3:
                self.coins+=1
            elif self.grid[y][x] == 5:
                self.level+=1
                self.teleport()
            self.grid[y][x] = 4
    
    #Function used to place blocks(Not currently used in the code)
    """
    def place(self,x,y):
        #Only place if blocks in inventory
        if self.inventory > 0:
            #Make sure no bugs happen when placing (placing on other blocks or placing them in the walls)
            if len(self.grid) == y or len(self.grid[self.height-1]) == x or y == -1 or x == -1 or self.grid[y][x] == 2:
                pass
            elif self.grid[y][x] == 3:
                self.objectives-=1
                self.grid[y][x] = 0
                self.inventory-=1
            else:
                #Store location of blocks (for purpuses not yet known)
                self.blocks.append([x,y])
                self.grid[y][x] = 2
                #subtract a block from the inventory
                self.inventory-=1
    """
    
#Manager
Main = int(input("Do you want to PLAY(1), CREATE(2), or IMPORT(3)"))

if Main == 1:
    #Play normally
    #Create game
    hello = Game("x")

    #Game_loop
    while True:
        hello.show_grid()
        print(f"{f.GREEN}Inventory : {f.BLUE}{hello.inventory} {f.GREEN}")
        print(f"{f.GREEN}Coins : {f.BLUE}{hello.coins}")
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
        """
        if keyboard.is_pressed(" "):
            hello.place((hello.lastx - hello.last2x)+hello.lastx,(hello.lasty - hello.last2y)+hello.lasty)
        """
        #Leave key
        if keyboard.is_pressed("l"):
            print(f"l key pressed! {f.RED}Leaving...{f.RESET}")
            sleep(3)
            os.system("cls")
            break
        #0.1 sec between updates, to prevent fast movement and also code crashing
        sleep(0.1)
        os.system("cls")
    
elif Main == 2:
    #Create a map
    import DD_Creator as DD
    hello = DD.Grid(int(input("Grid width > ")),int(input("Grid height > ")))

    #Game_loop
    while True:
        hello.show_grid()
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
    
elif Main == 3:
    level = input("Enter the level information generated with the LEVEL CREATOR here >> ")
    #Create game
    hello = Game(level)

    #Game_loop
    while True:
        hello.show_grid()
        print(f"{f.GREEN}Inventory : {f.BLUE}{hello.inventory} {f.GREEN}")
        print(f"{f.GREEN}Coins : {f.BLUE}{hello.coins}")
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
        """
        if keyboard.is_pressed(" "):
            hello.place((hello.lastx - hello.last2x)+hello.lastx,(hello.lasty - hello.last2y)+hello.lasty)
        """
        #Leave key
        if keyboard.is_pressed("l"):
            print(f"l key pressed! {f.RED}Leaving...{f.RESET}")
            sleep(3)
            os.system("cls")
            break
        #0.1 sec between updates, to prevent fast movement and also code crashing
        sleep(0.1)
        os.system("cls")

