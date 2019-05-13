
import random

# Create a rock/paper/scissors REPL loop
# Have a computer AI to play against us
# Keep track of the score
# Rules: r beats s, s beats p, p beats r

# Read
# Eval
# Print
# Loop

wins = 0
losses = 0
ties = 0
choices = ['r', 'p', 's']


def compare_answers(player_choice, ai_choice):
    # changes variables to global scope
    global ties
    global wins
    global losses
    if player_choice == ai_choice:
        print("You tie.")
        ties += 1
    # check if player entered losing input
    elif player_choice == 'p' and ai_choice == 's' or player_choice == 'r' and ai_choice == 'p' or player_choice == 's' and ai_choice == 'r':
        losses += 1
        print("You lose")
    # otherwise they win
    else:
        wins += 1
        print("You win!")


# Loop
while True:
    print(f"Score: {wins} - {losses} - {ties}")
    # Reads
    cmd = input("\nChoose r/p/s: ")
    # AI picks a random choice from r/p/s
    # Eval starts
    ai_choice = choices[random.randrange(3)]
    print(f"Computer chose {ai_choice}")
    if cmd == "q":
        print("Goodbye!")
        break
    elif cmd == 'r' or cmd == 'p' or cmd == 's':
        compare_answers(cmd, ai_choice)
    else:
        print("I do not understand that command.")
