import random as r 

attempts = 0 
number =  r.randint(1,100)
while True:
    guess = input("Guess a number between 1 and 100: ")
    attempts += 1
    try:
        guess = int(guess)
    except ValueError:
        print("Invalid Input Must Be a Number")
        continue
    if guess < number:
        print("Too Low")
    elif guess > number:
        print("Too High")
    else:
        print(f"Correct! You guessed the number in {attempts} attempts.")
        break