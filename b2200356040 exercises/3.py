import random
random_number = random.randint(0, 51)
while True:
    guess = int(input("Enter a number "))
    if guess > random_number:
        print("Decrease your number")
    elif guess < random_number:
        print("Increase your number")
    else:
        print("Your guess is correct")
