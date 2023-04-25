import random

# Define symbols that player and npc can select
MOVES = ["Rock","Scissor","Paper"]

# Creating a npc class to control the computer's moves
class Computer():

    def __init__(self) -> None:
        print("Computer is created".center(50,"-"))

    def select_move(self):
        computer_choice = str(random.choice(MOVES))
        print(f"Npc selected {computer_choice}")
        return computer_choice
    
# Creating a player class to control the user's moves
class Player():

    def __init__(self) -> None:
        print("Player is created".center(50,"-"))

    def select_move(self):
        print("List of moves you can select.")
        for m in MOVES:
            print("-" + m)
        choice = input("Please select your move: ")
        print(f"You selected {choice}")
        return choice

# Creating the game class to handle the game's flow
class Game():
    
    # Initializing the components that need to play game
    def __init__(self) -> None:
        self.computer = Computer()
        self.player = Player()

    # Start the game    
    def start_game(self):
        print("Game is started".center(50,"-"))
        self.current_round = 1
        self.display_rules()
        self.start_round()

    # Display the game's rules to player before game
    def display_rules(self):
        print("Welcome to game. You should write your answer properly.")
        print("Start with upper case in your answer.")
        print("Paper wins against Rock.")
        print("Rock wins against Scissor.")
        print("Scissor win against Paper.")
        print("Good luck !")
    # Start the tour to play
    def start_round(self):

        print(f"{self.current_round}. round is started".center(100,"-"))
        self.current_round +=1
        player_choice = self.player.select_move()
        computer_choice = self.computer.select_move()
        self.determine_winner(player_choice,computer_choice)

    # Checks who win 
    def determine_winner(self,player_choice,computer_choice):
        if player_choice == "Paper" and computer_choice == MOVES[2]:
            self.start_round()
        elif player_choice == "Paper" and computer_choice == MOVES[1]:
            self.game_over("NPC")
        elif player_choice == "Paper" and computer_choice == MOVES[0]:
            self.game_over("PLAYER")
        elif player_choice == "Rock" and computer_choice == MOVES[2]:
            self.game_over("NPC")
        elif player_choice == "Rock" and computer_choice == MOVES[1]:
            self.game_over("PLAYER")
        elif player_choice == "Rock" and computer_choice == MOVES[0]:
            self.start_round()
        elif player_choice == "Scissor" and computer_choice == MOVES[2]:
            self.game_over("PLAYER")
        elif player_choice == "Scissor" and computer_choice == MOVES[1]:
            self.start_round()
        elif player_choice == "Scissor" and computer_choice == MOVES[0]:
            self.game_over("NPC")
    # Finised game and announce the winner. Ask for another round.
    def game_over(self,winner):
        print(f"{winner} win the game. Do you want to play again ? (y/n)")
        while True:
            answer = input("Please enter your answer: ")
            if answer == "y":
                self.start_game()
                break
            elif answer == "n":
                print("Game is finished. Thanks for playing.")
                break
            else:
                print("You typed a wrong input. Please try again.\n")
# Create a game instant and start the game.
game = Game()
game.start_game()