# Name Count Program
# Written by Wesley Greer on 3/27/2026

# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

def count_file_lines():
    ######################
    with open(names.txt, 'r') as f:
        name_count = sum(1 for line in f)
    print(f"The total number of names is: {name_count}")
    ######################
    print('In the count_file_lines function')



# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()
