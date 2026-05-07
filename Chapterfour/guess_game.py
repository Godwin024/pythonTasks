import random

play_again = "yes"

while play_again == "yes":

    secret_number = random.randint(1, 1000)

    print("Guess my number between 1 and 1000 with the fewest guesses:")

    guess = int(input("Enter your guess: "))

    while guess != secret_number:

        if guess > secret_number:
            print("Too high. Try again.")

        else:
            print("Too low. Try again.")

        guess = int(input("Enter your guess number: "))

    print("Congratulations. You guessed the number!")

    play_again = input("Do you want to play again? (yes or no): ").lower()
