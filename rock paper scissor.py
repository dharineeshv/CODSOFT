import random

def rock_game(user, computer, user_score, computer_score):
    if user.lower() == computer.lower():
        print("It's a tie!")
    elif (user.lower() == "rock" and computer.lower() == "scissors") or \
         (user.lower() == "paper" and computer.lower() == "rock") or \
         (user.lower() == "scissors" and computer.lower() == "paper"):
        print("User wins!")
        user_score += 1
    elif (user.lower() == "rock" and computer.lower() == "paper") or \
         (user.lower() == "paper" and computer.lower() == "scissors") or \
         (user.lower() == "scissors" and computer.lower() == "rock"):
        print("Computer wins!")
        computer_score += 1
    else:
        print("Invalid input!")

    return user_score, computer_score

def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter rock/paper/scissors or enter 'end' to finish the game: ")
        if user_choice.lower() == "end":
            print("Thank you for playing!")
            if user_score > computer_score:
                print("Congrats!!! You Win!!!")
            elif user_score < computer_score:
                print("Oops!!! You Lose!!!")
                
            else:
                print("It's a tie!")
            break
        elif user_choice.lower() in ["rock", "paper", "scissors"]:
            computer_choice = random.choice(["rock", "paper", "scissors"])
            print(f"Computer chose {computer_choice}")
            user_score, computer_score = rock_game(user_choice, computer_choice, user_score, computer_score)
        else:
            print("Invalid input, please enter rock, paper, or scissors.")

main()
