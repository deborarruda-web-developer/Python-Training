"""
Create a Rock Paper Scissors game where the player inputs their choice
and plays against a computer that randomly selects its move,
with the game showing who won each round.
Add a score counter that tracks player and computer wins,
and allow the game to continue until the player types "quit".
"""
import random
def get_computer_choice():
    """Return a random choice for the computer's move in a rock-paper-scissors game.

    The function selects and returns one of the strings 'rock', 'paper', or 'scissors'
    at random (using the random.choice function). This is intended to represent the
    computer's move in a single round of the game.

    Returns:
        str: One of 'rock', 'paper', or 'scissors', chosen uniformly at random.

    Example:
        >>> choice = get_computer_choice()
        >>> choice in {'rock', 'paper', 'scissors'}
        True
    """
    return random.choice(['rock', 'paper', 'scissors'])
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif ((player == 'rock' and computer == 'scissors') or
          (player == 'paper' and computer == 'rock') or
          (player == 'scissors' and computer == 'paper')):
        return "You win!"
    else:
        return "Computer wins!"
def play_game():
    player_score = 0
    computer_score = 0
    # allow shorthand: r -> rock, p -> paper, s -> scissors, q -> quit
    short_map = {'r': 'rock', 'p': 'paper', 's': 'scissors', 'q': 'quit'}
    valid_choices = ['rock', 'paper', 'scissors']
    while True:
        player_choice = input("Enter rock(r), paper(p), scissors(s) or quit(q) to exit: ").lower().strip()
        # map short input (r/p/s/q) to full word first so 'q' becomes 'quit'
        if player_choice in short_map:
            player_choice = short_map[player_choice]
        if player_choice == 'quit':
            print("Thanks for playing!")
            break

        if player_choice not in valid_choices:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        print(result)
        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        print(f"Score - You: {player_score}, Computer: {computer_score}")
if __name__ == "__main__":
    play_game()
