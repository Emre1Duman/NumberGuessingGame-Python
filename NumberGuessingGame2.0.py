import random, art

random_number = random.randint(0,100)

EASY_LEVEL = 10
HARD_LEVEL = 5


def check_answer(guess, random_number, attempts):
    """Checks answer against guess. Returns number of attempts remaining"""
    if guess > random_number:
        print("Too high.")
        return attempts - 1
    elif guess < random_number:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You got it! The answer was {random_number}")


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    print(art.logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100. ")
    attempts = set_difficulty()
    

    guess = 0
    while guess != random_number:
        print(f"You have {attempts} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))
        attempts = check_answer(guess,random_number, attempts)
        if attempts == 0:
            print("You've run out of guesses, you lose")
            return #Returning will exit functions, hence breaking the while loop
        elif guess != random_number:
            print("Guess agan.")


game()