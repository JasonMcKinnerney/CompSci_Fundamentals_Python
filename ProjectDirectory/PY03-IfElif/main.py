########################
#Jason McKinnerney
#COSC 1336-007
#Coding 03: Decision Making
#Ask for input of 1 or 2 and print corresponding messages based on input including error
########################
number = input("Enter 1 or 2: ")
if number.isdigit():
    number = int(number)  
    if  number >= 1 and number <=2:
        if number == 1:
            print("Programming is fun!")
        elif number == 2:
            print("You're getting the hang of this.")
        else:
            print("Sorry, that isn't a 1 or 2")
    else:
        print("Sorry, that isn't a 1 or 2")
else:
        print("Sorry, that isn't a 1 or 2")