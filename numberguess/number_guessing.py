#!/usr/bin/python3

#For generating random numbers
import random
#For using the log math function
import math

lowerbound = int(input('Enter the lowerbound: ')) #Prompt user input for lowerbound
upperbound = int(input('Enter the upperbound: '))#Prompt user input for the upperbound

num_guesses = round(math.log(upperbound - lowerbound + 1, 2))#Calculate the number of guesses based on the upper and lower bounds
x = random.randint(lowerbound, upperbound)#Generate a random number to be guessed
print(f"\nYou have only {num_guesses} chances to guess the integer!\n")
count = 0 #Track the number of guesses made

while count < num_guesses: #Enter a continous loop of guesses
    count += 1 #Start the count
    guess = int(input('Guess a number: ')) #Ask for the guess from the player

    if x == guess:
        print(f"Congratulations, you did it in {count} tries!")
        break
    
    elif x > guess:
        print("You guessed too small!, Don't give up, try again.")

    elif x < guess:
        print("You guessed too high!, Don't give up try again")

if count >= num_guesses:
    print(f"\nThe number is {x} ;\)")
    print("\nBetter luck next time!")
