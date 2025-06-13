import random
import gavel_art
print(gavel_art.art)
print('Welcome to the number guessing game game')
print("I've a number between 1 and 100, can you guess it?")

def number_game():
    game_level: str = input('choose the difficulty level: "hard" or "easy""\t')
    if game_level == 'hard':
        attempts = 5
    else:
        attempts = 10
    guess = -10
    target_number = random.randint(1, 101)
    min_bound = 1
    max_bound = 100
    while attempts > 0 and guess != target_number:
        print(f">>>>>>>>>>>>>>>>>>>>you have {attempts} attempts left<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        guess = int(input(f'--> guess a number between {min_bound} and {max_bound}"\t'))
        attempts -= 1
        if guess < target_number:
            print('your guess is too low')
            #min_bound = guess --> these will apply a searching algorithm
        elif guess > target_number:
            print('your guess is too high')
            #max_bound = guess --> these will apply a searching algorithm
    if guess == target_number:
        print(f'You win. you guessed the correct number: {target_number}')
    else:
        print(f'you guessed the wrong number. Correct number: {target_number}')


continue_choice = True
while continue_choice:
    number_game()
    continue_selection = input('do you want to continue? (y/n)')
    if continue_selection == 'n':
        continue_choice = False
        print('Thank you for playing')

