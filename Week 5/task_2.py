# Write a program that generates and displays random numbers between 0 and 10, only stopping when a 0 is generated.
# modify it so that if the random number is a 7, the program prints “Lucky 7!” after the normal output.
import random

count = 1

while True:
    num = random.randint(0, 10)
    if num == 7:
        print('Lucky 7!')
    else:
        print(f'Number {count} was {num}')
    if num == 0:
        break
    count += 1
