import random

n = random.randrange(1, 10)
guess = int(input("Enter any number: "))
while n!=guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter the number again: "))
    elif guess > n:
        print("Too high")
        guess = int(input("Enter the number again: "))
    else:
        break
print("You genius, you guessed it right!!")
