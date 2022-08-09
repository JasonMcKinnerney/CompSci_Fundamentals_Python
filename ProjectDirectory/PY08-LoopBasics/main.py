# #################
#Jason McKinnerney
#COSC 1336-007
#Coding 04: Loops
#Ask for input of 1 or 2 and print corresponding messages based on input including error
# #################
import random


MIN = -10
MAX = 10
ZERO = 0

choice = "y"

while choice == "y" or choice == "Y":
    random_num = random.randint(MIN,MAX)
    print("Random Number: ", random_num)
    if random_num < ZERO:
        for r in range(abs(random_num)):
            for c in range(r + 1):
                print('*', end='')
            print()
    elif random_num > ZERO:
        for r in range(random_num):
            for c in range(random_num - r):
                print('*', end='')
            print()
    else:
        for r in range(MAX):
            for c in range(MAX):
                if c == r:
                    print(' ', end='*')
                else:
                    print('*', end='')
            print()      
    choice = input("Do you wish to print another pattern (y/n)? ")

