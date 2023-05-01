from colorama import Fore as F
import keyboard
from time import sleep
import os
import random
from colorama import Fore as f

banner = f"""{F.LIGHTGREEN_EX}

     ___  _______  __    _  ___   _______  _______  _______    _______  _______  __   __  _______  _______ 
    |   ||   _   ||  |  | ||   | |       ||       ||       |  |       ||   _   ||  |_|  ||       ||       |
    |   ||  |_|  ||   |_| ||   | |_     _||   _   ||    _  |  |    ___||  |_|  ||       ||    ___||  _____|
    |   ||       ||       ||   |   |   |  |  | |  ||   |_| |  |   | __ |       ||       ||   |___ | |_____ 
 ___|   ||       ||  _    ||   |   |   |  |  |_|  ||    ___|  |   ||  ||       ||       ||    ___||_____  |
|       ||   _   || | |   ||   |   |   |  |       ||   |      |   |_| ||   _   || ||_|| ||   |___  _____| |
|_______||__| |__||_|  |__||___|   |___|  |_______||___|      |_______||__| |__||_|   |_||_______||_______|

"""
print(banner)

main = int(input("Que juego quieres jugar? (1 = Paint Simulator 202024, 2 = nada de momento)"))
if main == 1:
    import Paint_simulator_202024 as p
    hello = p.Grid(int(input("Grid width > ")),int(input("Grid height > ")))

    #Game_loop
    while True:
        hello.show_grid()
        print(f"{f.GREEN}Inventory : {f.BLUE}{hello.inventory} {f.GREEN}blocks")
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
            break
        #0.1 sec between updates, to prevent fast movement and also code crashing
        sleep(0.1)
        os.system("cls")
    print(f"l key pressed! {f.RED}Leaving...{f.RESET}")
    sleep(3)
    os.system("cls")
elif main == 2:
    import DeathDungeon as DD
    hello = DD.Game()
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
