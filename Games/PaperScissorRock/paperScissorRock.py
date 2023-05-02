import random

# Define moves that player and computer can select
MOVES = ["rock","scissor","paper"]

win_conditions = {
    "rock":{"Win":"Scissor","Lose":"Paper"},
    "scissor":{"Win":"Paper","Lose":"Rock"},
    "paper":{"Win":"Rock","Lose":"Scissor"}
}

# Creating a computer class to control the computer's moves
class Computer():

    def __init__(self) -> None:
        print("Computer is created".center(50,"-"))

    def select_move(self):
        computer_choice = str(random.choice(MOVES))
        print(f"Npc selected {computer_choice}")
        return computer_choice
    
# Creating a player class to control the players's moves
class Player():

    def __init__(self) -> None:
        print("Player is created".center(50,"-"))

    def select_move(self):
        print("List of moves you can select.")
        for m in MOVES:
            print("-" + m)
        choice = input("Please select your move: ").lower()
        if choice not in MOVES:
            raise Exception("Please type your choice correctly.")
        else:
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
        print("Welcome to game. You should write your answer correctly.")
        print("Start with upper case in your answer.")
        print("Paper wins against Rock.")
        print("Rock wins against Scissor.")
        print("Scissor win against Paper.")
        print("Good luck !")
    # Start the tour to play
    def start_round(self):

        print(f"{self.current_round}. round is started".center(100,"-"))
        self.current_round +=1
        while True:
            try:
                player_choice = self.player.select_move()
            except Exception as ex:
                print(ex)
            else:
                break
        computer_choice = self.computer.select_move().lower()
        self.determine_winner(player_choice,computer_choice)

    # Checks who win 
    def determine_winner(self,player_choice,computer_choice):
        if player_choice in (win_conditions[computer_choice]["Win"]).lower():
            try:
                self.game_over("Computer")
            except Exception as ex:
                print(ex)
        elif player_choice in (win_conditions[computer_choice]["Lose"]).lower():
            try:
                self.game_over("Player")
            except Exception as ex:
                print(ex)
        else:
            self.start_round()


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
                raise Exception("You typed a wrong input.")
# Create a game instant and start the game.
game = Game()
game.start_game()