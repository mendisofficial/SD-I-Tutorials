# Write a program to implement a “lap time recorder” that allows the user to input the times taken for a car to complete multiple laps of a racetrack, and see some basic statistics about the lap times.

total = 0
fastest = None
slowest = None

laps = int(input('How many laps will you be entering? '))

for i in range(laps):
    time = float(input(f'Enter the time for lap {i + 1} of {laps}: '))
    total += time
    if fastest is None or time < fastest:
        fastest = time
    if slowest is None or time > slowest:
        slowest = time

average = round(total / laps, 2)

print(f'Total time: {total}')
print(f'Fastest time: {fastest}')
print(f'Slowest time: {slowest}')
print(f'Average time: {average}')
