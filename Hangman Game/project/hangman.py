import random

# Predefined list of exactly 5 words used by the game.
WORDS = ["python", "hangman", "computer", "keyboard", "monitor"]

# Maximum number of incorrect guesses allowed before the player loses.
MAX_INCORRECT = 6


def play_game():
    """Run a single round of the Hangman game from start to finish."""

    # Step 1: randomly pick one word from the predefined list.
    word = random.choice(WORDS)

    # Track which letters the player has guessed so far (both correct and wrong).
    guessed_letters = set()

    # Count of wrong guesses the player has made.
    incorrect_guesses = 0

    # Build the initial display: one underscore per letter in the word.
    display = ["_" for _ in word]

    print("Welcome to Hangman!")
    print("Guess one letter at a time. You have", MAX_INCORRECT, "wrong guesses allowed.\n")

    # Main game loop: keep going until the player wins or runs out of guesses.
    while incorrect_guesses < MAX_INCORRECT and "_" in display:

        # Show the current state of the word and the letters already guessed.
        print("Word:", " ".join(display))
        print("Guessed letters:", " ".join(sorted(guessed_letters)) if guessed_letters else "none")
        print("Wrong guesses left:", MAX_INCORRECT - incorrect_guesses)

        # Read the player's guess and validate the input.
        guess = input("Enter a letter: ").strip().lower()

        # Input validation: must be exactly one alphabet character.
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabet letter.\n")
            continue

        # Prevent duplicate guesses: if the letter was already tried, ask again.
        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.\n")
            continue

        # Record the guess now that we know it is valid and new.
        guessed_letters.add(guess)

        # Correct guess: reveal every matching position in the display.
        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    display[index] = guess
            print("Good guess!\n")
        else:
            # Wrong guess: use up one of the remaining attempts.
            incorrect_guesses += 1
            print("Wrong guess!\n")

    # The loop ended: figure out whether the player won or lost.
    if "_" not in display:
        print("Word:", " ".join(display))
        print("Congratulations! You guessed the word:", word)
    else:
        print("Out of guesses! You lost. The word was:", word)


def main():
    """Entry point: play rounds repeatedly until the player chooses to stop."""
    while True:
        play_game()

        # Ask whether the player wants another round.
        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("Thanks for playing Hangman. Goodbye!")
            break


if __name__ == "__main__":
    main()
