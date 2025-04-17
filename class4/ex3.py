# the program randomly selects a number within a range, and the user has to guess the number. the program provides hints if the guess is too high or too low

# Algorithm

# randomly select a number
# ask user to guess the number
# if correct, say correct
# if mot correct show hint and keep repeating till user guess the number

random_number = 5
user_guess = 0

while user_guess != random_number:
    user_guess = int(input("Guess the number: "))
    if user_guess == random_number:
        print("you guessed it right")
    else:
        if user_guess > random_number:
            print("your guess is too high")
        else:
            print("your guess is too low")