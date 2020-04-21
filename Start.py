from tkinter import *

screenWidth = 1680
screenHeight = 1050
windowWidth = 650
windowHeight = 400

instructions = ["Welcome to Try2Survive®. You are the captain of a spaceship called Gianni and your job is to avoid "
                "getting hit by dangerous asteroids. Every time you get hit by one you will lose your health and score "
                "relative to the speed of an asteroid, so watch out for the fast ones. Good luck and Try2Survive."]

class Game(Frame):
    def __init__(self, root):
        self.root = root
        self.root.title('Try2Survive')  # postavlja naslov prozora
        self.root.resizable(False, False)
        self.root.geometry(
            str(windowWidth) + 'x' + str(windowHeight) + '+' + str(screenWidth // 2 - windowWidth // 2) + '+' + str(
                screenHeight // 2 - windowHeight // 2))
        super().__init__(self.root)
        self.createInterface()
        return

    def createInterface(self):
        self.grid(column=3, row=3)
        return


game = Game(Tk())
game.mainloop()
