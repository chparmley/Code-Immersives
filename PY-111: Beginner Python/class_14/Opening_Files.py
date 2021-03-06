
# -----[WORKING WITH FILES]-----
#


# Accessing files is done using the open() function
open('test_file.txt')

# Before working with its contents, they should be stored to a variable
our_file = open('test_file.txt')

# There are four modes to open files with, r(EAD) w(RITE) a(PPEND) x(CLUSIVE)
#  Choose the appropriate one depending on what you want to do with the 
#   file, and place it's correspoding letter as the second argument of the open() function
our_file = open('test_file.txt', 'r')
for line in our_file:
    print(line)

# Once done working with the file, close it to free up memory and usage of the file
our_file.close()