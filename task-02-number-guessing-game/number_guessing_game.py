import random

print("Welcome to Number Guessing Game!")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess_number = int(input("\nGuess a number: "))

        if guess_number < 1 or guess_number > 100:
            print("Please guess a number between 1 and 100.")
            continue

        attempts += 1

        if guess_number == secret_number:
            attempt_word = "attempt" if attempts == 1 else "attempts"
            print(f"Congratulations 🎉 You guessed the number in {attempts} {attempt_word}.")
            break
        elif guess_number > secret_number:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")
    except ValueError:
        print("Please enter a valid whole number!")