# Random Number File Program
# Written By Wesley Greer on 3/27/2026

import random

print('This program allows you to write up to 1000 random numbers to a file.')
with open('numbers.txt' 'w') as num:
    try:
        file_size = int(input('How many random numbers would you like to write to the file? '))
        if file_size > 1000 or file_size < 0:
            print('Please enter a number equal to or less than 1000, and make sure it is a positive integer.')
            file_size = int(input('How many random numbers would you like to write to the file? '))
        for n in range(file_size):
            num.write(random.randint(1,500),'/n')
    except ValueError:
        print('Error: You must enter an integer. Your number cannot have decimals. (e.g. 3.5, .25)')
