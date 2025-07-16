import random

secret_number = random.randint(1, 100)
attempts = 3
while attempts > 0:
    guess = int(input("Guess the secret number between 1 and 100: "))
    if guess == secret_number:
        print("Congratulations! You've guessed the secret number.")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    
    attempts -= 1
    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")
        
