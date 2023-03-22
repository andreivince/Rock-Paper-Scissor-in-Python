import random
user_points = 0
npc_points = 0

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
        else:
            print("That's not a choice.")

game()