import random
import utility as ul

x = 1
#user types the lowest limit for the number gen
low_lim = int(input("Min: "))
#user types the higest lim it for the number gen
high_lim = int(input("Max: "))
#generates the answer
number = random.randint(low_lim, high_lim)

attempts = int(input("How many attempts are allowed?: "))

while True:
    #user inputs the guess
    guess = input("Guess the number:\n")
    #checks if the guess is corret
    result = ul.lengthChecker(int, guess, number)
    if attempts == 1:
        print("You have used up all the attempts, good luck next game!")
        ul.anyKey()
        break
    else:
        pass
    if result == 'pass':
        if x == 1:
            print("You guessed it! the number was " + str(number) + ". You got it on the first try!")
            ul.anyKey()
            break
        else:
            print("You guessed it! the number was " + str(number) + ". It only took you " + str(x) + " tries!")
            ul.anyKey()
            break
    elif result == 'short':
        attempts -= 1
        print(guess + " is lower than the answer.\n" + "You have " + str(attempts) + " attempts left.")
        x += 1
    elif result == 'long':
        attempts -= 1
        print(guess + " is higher than the answer.\n" + "You have " + str(attempts) + " attempts left.")
        x += 1