import random
'''
#Guessing Game with only 10 guesses!

def total_guesses():
    total = 0
    for i in range(11):
        new_number = int(input("Enter a number: "))
        total += new_number #Total = new number plus total
    print("The total amount of guesses is: ", total)
    return
total_guesses()
'''
#this DOESNT MAKE SENSE BECAUSE IT ADDES EVERYTHING TOGETHER AAGH n mfh,k

#end loops with the WORD break

#Shake my head let's let Irimina teach us functions I'll figure it out later

#Actual guessing game! Based off of sample code

print("Hello! Welcome to my guessing game! What's your name?")
usr = input("Name: ")
print("Welcome, ", usr, "! Today we will guess a random number. It is up to discover this number. Let's get started.")
print("This number will be from 1 to 100.")
total_guesses = 0 #This is used to calculate the users guesses.
number = random.randrange(101)
print("Go ahead, guess a random number!")
while total_guesses <= 5:
    guess = int(input("Guess: "))
    total_guesses = total_guesses + 1
    if guess > number:
        print("Your guess was too high! Try again,", usr, "!")
    elif guess < number:
        print("Your guess was too low! Try again,", usr, "!")
    elif guess == number:
        print("Aye! you got it! Congratulations,", usr, "!")
        total_guesses = 5
        break
    if total_guesses == 5:
        print("Sorry", usr, "You ran outta guesses! Please try again.")
        break
