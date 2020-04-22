from tkinter import *
import pathlib
import Main

screenWidth = 1680
screenHeight = 1050
windowWidth = 630
windowHeight = 340

instructions = ["Welcome to Try2Survive®.",
                "You are the captain of a spaceship called Gianni and your job is to",
                "avoid getting hit by dangerous asteroids. Every time you get hit by",
                "one you will lose your health and score relative to the speed of an",
                "asteroid, so watch out for the fast ones.",
                "Good luck and Try2Survive.",
                "\nAre you ready?"]

font = ("Comic Sans MS", 20, "italic")

black = 'black'
white = 'white'
gold = 'gold'

class Game(Frame):
    def __init__(self, root):
        self.root = root
        self.root.title('Try2Survive')  # postavlja naslov prozora
        self.root.resizable(False, False)
        self.root.geometry(str(windowWidth) + 'x' + str(windowHeight) + '+' + str(screenWidth // 2 - windowWidth // 2)
                           + '+' + str(screenHeight // 2 - windowHeight // 2))
        super().__init__(self.root)
        self.grid()
        self.createInterface()
        return

    def createInterface(self):
        for i in range(0, len(instructions)):
            label = Label(self, text = instructions[i], bg = black, fg = gold, font = font)
            label.grid(row = i, column = 1, sticky = W + E)
        button = Button(self, text = 'PLAY GAME', bg = black, fg = gold, font = font, command = self.buttonClicked, height = '2')
        button.grid(row = i + 1, column = 1, sticky = W + E, rowspan = 2)
        return

    def buttonClicked(self):
        Main.main()
        print("Button pressed")


game = Game(Tk())
game.mainloop()
