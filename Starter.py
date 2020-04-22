from Config import *
from tkinter import *
from Game import Game

class Starter(Frame):
    def __init__(self, root):
        self.root = root
        self.root.title('Try2Survive')  # postavlja naslov prozora
        self.root.resizable(False, False)
        self.width = 800
        self.height = 380
        self.root.geometry(str(self.width) + 'x' + str(self.height) + '+' + str(windowWidth // 2 - self.width // 2)
                           + '+' + str(windowHeight // 2 - self.height // 2))
        super().__init__(self.root)

        self.font = ("Comic Sans MS", 18, "italic")
        self.instructions = ["Welcome to Try2Survive®.",
                             "You are the captain of a spaceship called Gianni and your job is to",
                             "avoid getting hit by dangerous asteroids. Every time you get hit by",
                             "an asteroid you lose your health and score relative to the speed of",
                             "the asteroid, so watch out for the fast ones.",
                             "Good luck and Try2Survive.",
                             "\nAre you ready?"]

        self.grid(column=1)
        self.createInterface()
        return

    def createInterface(self):
        for i in range(0, len(self.instructions)):
            label = Label(self.root, text=self.instructions[i], bg='black', fg='gold', font=self.font)
            label.grid(row=i, column=0, sticky=W + E)

        button = Button(self.root, text='PLAY GAME', bg='gold', fg='black', font=self.font, command=self.buttonClicked,
                        height='2')
        button.grid(row=i + 1, column=0, sticky=W + E)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(i + 1, weight=1)
        return

    def buttonClicked(self):
        self.root.destroy()
        game = Game()
        game.main()

if __name__ == '__main__':
    starter = Starter(Tk())
    starter.mainloop()