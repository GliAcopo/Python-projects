import sys, time
import random
from random import randint

#printslow process
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)

human_points = 0
machine_points = 0

human_response = 0
computer_response = 0


#first round
def first_round():
    #resettiamo i valori e li facciamo tornare a 0
    
    human_response = 0
    computer_response = 0
    
    #asking user input phase
    print_slow("First round out of 3\n")
    print_slow("what do you choose?\n 1. Rock\n 2. Paper\n 3. Scissor\n")
    human_response = int(input("write a number --> "))
    #random computer response
    computer_response = randint(1, 3)
    print_slow("\nmatch started!\n")
    
       
    #we are declaring the trows
    #your trow
    print_slow("your answer was ")
    if human_response == 1:
        print_slow("Rock\n")
    elif human_response == 2:
        print_slow("Paper\n")
    elif human_response == 3:
        print_slow("Scissor\n")
    else:
        print_slow("Invalid user input at first round!\n")
        first_round()
    
    #machine's trow
    print_slow("computer's answer was ")
    if computer_response == 1:
        print_slow("Rock\n")
    elif computer_response == 2:
        print_slow("Paper\n")
    elif computer_response == 3:
        print_slow("Scissor\n")
    else:
        print_slow("Invalid computer input at first round!\n")
        first_round()

   #tutti i casi in cui finisce in PAREGGIO 
    if (computer_response == 1 and human_response == 1) or (computer_response == 2 and human_response == 2) or (computer_response == 3 and human_response == 3):
        print_slow("stalemate!\n\n")        
    #tutti i casi in cui finisce in UOMO CHE VINCE
    elif (computer_response == 3 and human_response == 1) or (computer_response == 1 and human_response == 2) or (computer_response == 2 and human_response == 3):
        human_points == human_points + 1
        print_slow("human's victory!\n\n")
    #tutti i casi in cui finisce in MACCHINA CHE VINCE
    elif (computer_response == 1 and human_response == 3) or (computer_response == 2 and human_response == 1) or (computer_response == 3 and human_response == 2):
        machine_points == machine_points + 1
        print_slow("machine's victory!\n\n")
    else:
        print_slow("oh no... something got wrong at the point calculation in the first round...\n")
        first_round()



#second round
def second_round():
    #resettiamo i valori e li facciamo tornare a 0
    
    human_response = 0
    computer_response = 0
    
    #asking user input phase
    print_slow("Second round out of 3\n")
    print_slow("what do you choose?\n 1. Rock\n 2. Paper\n 3. Scissor\n")
    human_response = int(input("write a number --> "))
    #random computer response
    computer_response = randint(1, 3)
    print_slow("\nmatch started!\n")
    
       
    #we are declaring the trows
    #your trow
    print_slow("your answer was ")
    if human_response == 1:
        print_slow("Rock\n")
    elif human_response == 2:
        print_slow("Paper\n")
    elif human_response == 3:
        print_slow("Scissor\n")
    else:
        print_slow("Invalid user input at second round!\n")
        second_round()
    
    #machine's trow
    print_slow("computer's answer was ")
    if computer_response == 1:
        print_slow("Rock\n")
    elif computer_response == 2:
        print_slow("Paper\n")
    elif computer_response == 3:
        print_slow("Scissor\n")
    else:
        print_slow("Invalid computer input at second round!\n")
        second_round()

   #tutti i casi in cui finisce in PAREGGIO 
    if (computer_response == 1 and human_response == 1) or (computer_response == 2 and human_response == 2) or (computer_response == 3 and human_response == 3):
        print_slow("stalemate!\n\n")       
    #tutti i casi in cui finisce in UOMO CHE VINCE
    elif (computer_response == 3 and human_response == 1) or (computer_response == 1 and human_response == 2) or (computer_response == 2 and human_response == 3):
        human_points == human_points + 1
        print_slow("human's victory!\n\n")
    #tutti i casi in cui finisce in MACCHINA CHE VINCE
    elif (computer_response == 1 and human_response == 3) or (computer_response == 2 and human_response == 1) or (computer_response == 3 and human_response == 2):
        machine_points == machine_points + 1
        print_slow("machine's victory!\n\n")
    else:
        print_slow("oh no... something got wrong at the point calculation in the second round...\n")
        second_round()



#third round
def third_round():
    #resettiamo i valori e li facciamo tornare a 0
    
    human_response = 0
    computer_response = 0
    
    #asking user input phase
    print_slow("Third round out of 3\n")
    print_slow("what do you choose?\n 1. Rock\n 2. Paper\n 3. Scissor\n")
    human_response = int(input("write a number --> "))
    #random computer response
    computer_response = randint(1, 3)
    print_slow("\nmatch started!\n")
    
       
    #we have to transform the response numbers in strings for the user
    #your trow
    print_slow("your answer was ")
    if human_response == 1:
        print_slow("Rock\n")
    elif human_response == 2:
        print_slow("Paper\n")
    elif human_response == 3:
        print_slow("Scissor\n")
    else:
        print_slow("Invalid user input at third round!\n")
        third_round()
    
    #machine's trow
    print_slow("computer's answer was ")
    if computer_response == 1:
        print_slow("Rock\n")
    elif computer_response == 2:
        print_slow("Paper\n")
    elif computer_response == 3:
        print_slow("Scissor\n")
    else:
        print_slow("Invalid computer input at third round!\n")
        third_round()

   #tutti i casi in cui finisce in PAREGGIO 
    if (computer_response == 1 and human_response == 1) or (computer_response == 2 and human_response == 2) or (computer_response == 3 and human_response == 3):
        print_slow("stalemate!\n\n")        
    #tutti i casi in cui finisce in UOMO CHE VINCE
    elif (computer_response == 3 and human_response == 1) or (computer_response == 1 and human_response == 2) or (computer_response == 2 and human_response == 3):
        human_points == human_points + 1
        print_slow("human's victory!\n\n")
    #tutti i casi in cui finisce in MACCHINA CHE VINCE
    elif (computer_response == 1 and human_response == 3) or (computer_response == 2 and human_response == 1) or (computer_response == 3 and human_response == 2):
        machine_points == machine_points + 1
        print_slow("machine's victory!\n\n")
    else:
        print_slow("oh no... something got wrong at the point calculation in the third round...\n")
        third_round()



def win_declaration():
    if human_points == 3:
        print_slow("Absolute victory by machines!\n")
    elif machine_points == 3:
        print_slow("Absolute victory by machines!\n")
    elif human_points > machine_points:
        print_slow("Victory of the humans!\n")
    elif machine_points > human_points:
        print_slow("Victory of the machines!\n")
    elif machine_points > human_points:
        print_slow("Complete stalemate?!")
    else:
        print_slow("Invalid win declaration!\n")

    
#main function
def main():
    print_slow("Hey! Welcome to Rock, Paper, Scissors!\n")
    print_slow("you're going to dispute a mach with the computer of 3 rounds, good luck!\n")
    first_round()
    second_round()
    third_round()
    win_declaration()


main()
retry = 0
#asking for retry
print_slow("Do you wish to retry?\n")
print_slow("1. yes\n2. no\n")
retry = input()
if retry == 1:
    print_slow("I wish you good luck!\n")
    main()
elif retry == 2:
    print_slow("Ok then, see you soon\n")
    quit
else:
    print_slow("Invalid retry...")
    quit