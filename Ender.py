from Loader import *
from tkinter import *

class Ender(Frame):
    def __init__(self, root, score):
        self.root = root
        self.root.title('Try2Survive')  # postavlja naslov prozora
        self.root.resizable(False, False)
        self.width = 400
        self.height = 180

        self.root.geometry(str(self.width) + 'x' + str(self.height) + '+' + str(windowWidth // 2 - self.width // 2)
                           + '+' + str(windowHeight // 2 - self.height // 2))
        super().__init__(self.root)

        self.font = ("Comic Sans MS", 18, "italic")
        self.instructions = ["Game over. Your score is: " + str(score),
                             "\nStart again?"]

        self.grid(column=2, sticky=N+S+E+W)
        self.createInterface()
        return

    def createInterface(self):
        for i in range(0, len(self.instructions)):
            label = Label(self.root, text=self.instructions[i], bg='black', fg='gold', font=self.font)
            label.grid(row=i, column=0, columnspan=2, sticky=N+S+W+E)
            self.root.grid_columnconfigure(0, weight=1)

        button1 = Button(self.root, text='NO', bg='gold', fg='black', font=self.font, command=self.closeWindow)
        button1.grid(row=i + 1, column=0, sticky=N + S + W + E)
        self.root.grid_columnconfigure(0, weight=1)

        button2 = Button(self.root, text='YES', bg='gold', fg='black', font=self.font, command=self.startAgain)
        button2.grid(row=i + 1, column=1, sticky=N + S + W + E)
        self.root.grid_columnconfigure(1, weight=1)

        self.root.grid_rowconfigure(i, weight=3)
        self.root.grid_rowconfigure(i + 1, weight=2)
        return

    def closeWindow(self):
        self.root.destroy()
        return False

    def startAgain(self):
        self.root.destroy()
        pygame.init()
        loadData()
        from Game import Game
        game = Game()
        game.main()
        return True

if __name__ == '__main__':
    ender = Ender(Tk(), 324)
    ender.mainloop()
