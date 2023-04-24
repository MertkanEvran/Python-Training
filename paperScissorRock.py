import random

# Define symbols that player and npc can select
symbols = ["Rock","Scissor","Paper"]

# Creating a npc class to control the computer's moves
class Npc():

    def __init__(self) -> None:
        print("Npc is created".center(50,"-"))

    def makeChoice(self):
        ncpChoice = str(random.choice(symbols))
        print(f"Npc selected {ncpChoice}")
        return ncpChoice
    
# Creating a player class to control the user's moves
class Player():

    def __init__(self) -> None:
        print("Player is created".center(50,"-"))

    def selectChoice(self):
        print("List of choice.")
        for s in symbols:
            print("-" + s)
        answer = input("Please select your move: ")
        print(f"You selected {answer}")
        return answer

# Creating the game class to handle the game's flow
class Game():
    
    # Initializing the components that need to play game
    def __init__(self) -> None:
        self.npc = Npc()
        self.player = Player()

    # Start the game    
    def startGame(self):
        print("Game is started".center(50,"-"))
        self.currentTour = 1
        self.displayRules()
        self.startTour()

    # Display the game's rules to player before game
    def displayRules(self):
        print("Welcome to game. You should write your answer properly. Start with upper case in your answer.\nPaper wins against Rock\nRock wins against Scissor\nScissor win against Paper.\nGood Luck...  ")
    
    # Start the tour to play
    def startTour(self):

        print(f"{self.currentTour}. tour is started".center(100,"-"))
        self.currentTour +=1
        playerChoice = self.player.selectChoice()
        npcChoice = self.npc.makeChoice()
        self.checkTheTour(playerChoice,npcChoice)

    # Checks that if any one win or lose
    def checkTheTour(self,playerChoice,npcChoice):
        if playerChoice == "Paper" and npcChoice == symbols[2]:
            self.startTour()
        elif playerChoice == "Paper" and npcChoice == symbols[1]:
            self.gameOver("NPC")
        elif playerChoice == "Paper" and npcChoice == symbols[0]:
            self.gameOver("PLAYER")
        elif playerChoice == "Rock" and npcChoice == symbols[2]:
            self.gameOver("NPC")
        elif playerChoice == "Rock" and npcChoice == symbols[1]:
            self.gameOver("PLAYER")
        elif playerChoice == "Rock" and npcChoice == symbols[0]:
            self.startTour()
        elif playerChoice == "Scissor" and npcChoice == symbols[2]:
            self.gameOver("PLAYER")
        elif playerChoice == "Scissor" and npcChoice == symbols[1]:
            self.startTour()
        elif playerChoice == "Scissor" and npcChoice == symbols[0]:
            self.gameOver("NPC")
        
    def gameOver(self,winner):
        print(f"{winner} win the game. Do you want to play again ? (y/n)")
        while True:
            answer = input("Please enter your answer: ")
            if answer == "y":
                self.startGame()
                break
            elif answer == "n":
                print("Game is finished. Thanks for playing.")
                break
            else:
                print("You typed a wrong input. Please try again.\n")
# Create a game instant and start the game.
game = Game()
game.startGame()