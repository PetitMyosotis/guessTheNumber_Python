import random

#get a random number
number = random.randrange(1, 100)

#ask for a guess
guess = int(input("My number is between 0 and 100. Make a guess !"))

# counter for the attempts
attempts = 0

while guess != number:
    if guess < 0 or guess > 100:
        print("My number is between 0 and 100.")
        attempts = attempts + 1
        guess = int(input("make a guess !"))
    elif guess < number:
        print("it's bigger")
        attempts = attempts + 1
        guess = int(input("make a guess !"))
    elif guess > number:
        print("it's lower")
        attempts = attempts + 1
        guess = int(input("make a guess !"))
if guess == number:
    print("You found it!")
    print("attempts: " + str(attempts))
