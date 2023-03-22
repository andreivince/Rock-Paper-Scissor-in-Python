import random
user_points = 0
npc_points = 0

# Function to play a game of Rock, Paper, Scissors
def game():
    global user_points
    global npc_points
    choices = ["rock", "scissor", "paper"]
    print("Let's play")
    while True:
        print("Rock, Paper, Scissors")
        print("3...")
        print("2...")
        print("1...")
        user_answer = input("Choice: ")
        npc_answer = random.choice(choices)

        # Check if user chose rock and NPC chose paper
        if user_answer.lower() == "rock" and npc_answer == "paper":
            print(f"You lost because you chose {user_answer} and the program chose {npc_answer}")
            npc_points += 1
            print(f"Program {npc_points} and User {user_points}")
            play_again = input("Would you like to play again? ")
            if play_again.lower() != "yes":
                print(f"Ok!! The final score is Program {npc_points} and User {user_points}")
                break
            else:
                game()
                
        # Check if user chose paper and NPC chose rock
        elif user_answer.lower() == "paper" and npc_answer == "rock":
            print(f"You win because you chose {user_answer} and the program chose {npc_answer}")
            user_points += 1
            print(f"Program {npc_points} and User {user_points}")
            play_again = input("Would you like to play again? ")
            if play_again.lower() != "yes":
                print(f"Ok!! The final score is Program {npc_points} and User {user_points}")
                break
            else:
                game()
                
        # Check if user chose scissor and NPC chose paper
        elif user_answer.lower() == "scissor" and npc_answer == "paper":
            print(f"You win because you chose {user_answer} and the program chose {npc_answer}")
            user_points += 1
            print(f"Program {npc_points} and User {user_points}")
            play_again = input("Would you like to play again? ")
            if play_again.lower() != "yes":
                print(f"Ok!! The final score is Program {npc_points} and User {user_points}")
                break
            else:
                game()
                
        # Check if user chose paper and NPC chose scissor
        elif user_answer.lower() == "paper" and npc_answer == "scissor":
            print(f"You lost because you chose {user_answer} and the program chose {npc_answer}")
            npc_points += 1
            print(f"Program {npc_points} and User {user_points}")
            play_again = input("Would you like to play again? ")
            if play_again.lower() != "yes":
                print(f"Ok!! The final score is Program {npc_points} and User {user_points}")
                break
            else:
                game()
                
        # Check if user chose scissor and NPC chose rock
        elif user_answer.lower() == "scissor" and npc_answer == "rock":
            print(f"You lost because you chose {user_answer} and the program chose {npc_answer}")
            npc_points += 1
            print(f"Program {npc_points} and User {user_points}")
            play_again = input("Would you like to play again? ")
            if play_again.lower() != "yes":
                print(f"Ok!! The final score is Program {npc_points} and User {user_points}")
                break
            else:
                game()
                
        # Check if user chose rock and NPC chose scissor
        elif user_answer.lower() == "rock" and npc_answer == "scissor":
            print(f"You win because you chose {user_answer} and the program chose {npc_answer}")
            user_points += 1
            print(f"Program {npc_points} and User {user_points}")
            play_again = input("Would you like to play again? ")
            if play_again.lower() != "yes":
                print(f"Ok!! The final score is Program {npc_points} and User {user_points}")
                break
            else:
                game()
                
        # If neither rock, paper, nor scissor was chosen, print error message
        else:
            print("That's not a choice.")

game()
