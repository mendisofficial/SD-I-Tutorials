import random

print('Guess the number between 1 and 100!')

num = random.randint(1, 100)

guess_count = 0

while True:
    guess = int(input('Enter your guess: '))
    guess_count += 1
    if guess < num:
        print('Too low!')
    elif guess > num:
        print('Too high!')
    else:
        print(f'{num} is correct, you win!')
        break

print(f'You got it in {guess_count}')
