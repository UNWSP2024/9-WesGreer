# Number File Average Program
# Written by Wesley Greer on 3/27/2026
def sum_numbers_from_file():
    ######################
    try:
        with open(numbers.txt, 'r') as num:
            numbers = [float(line.strip()) for line in num]
            average = sum(numbers) / len(numbers)
            print('The average of all the numbers within the file is:', average)
    except ValueError:
        print('ERROR: Non-numeric data was found within the file.')
    except ZeroDivisionError:
        print('ERROR: There are no numbers within the file.')
    except IOError:
        print('ERROR: File was not found.')
    ######################
    print('In the sum_numbers_from_file function')

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()
