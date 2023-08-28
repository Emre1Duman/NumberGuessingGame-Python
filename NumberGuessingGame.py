import random, art

random_number = random.randint(0,101)

print(art.logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100. ")

attempts = 0
endgame = False

difficulty = input("Choose a difficulty. Type 'easy' or 'hard'. ").lower()
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    print("Inavlid input")

while not endgame:
    if attempts == 0:
        print("You have run out of guesses, you lose :(")
        endgame = True
    else:
        print(f"You have {attempts} attempts remaining to guess the number.") 
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print(f"You got it! The answer was {random_number}")
            endgame = True       
        elif guess > random_number:
            print("Too high. Guess again!")
            attempts -= 1
        elif guess < random_number:
            print("Too low. Guess again!")
            attempts -= 1
        




