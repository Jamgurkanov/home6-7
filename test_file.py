import random

tries = 0
the_numbers = random.randint(1, 100)
while True:
    guess = int(input("your guess: "))
    if guess < the_numbers:
        print("your guess is too high")
        tries += 1
    elif guess > the_numbers:
        print("your guess is too low")
        tries += 1

    else:
        print("your guess is correct")
        print(f'{"your tries"} {tries}')
        print("molodec")
        break

