import random
import time

print("""
Welcome to number guessing game!
I am thinking of a number between 1-100
Let's see if you can guess it. Godspeed
""")
while True:
    number = random.randint(0,100)
    time.sleep(2)
    print("Ok, I have selected my number. Should we start?(y/n)")
    game_choice = input().lower()
    if game_choice == 'y':
        print("""What difficulty level would you prefer?
1. Easy(10 tries)
2. Medium(5 Tries)
3. Hard(3 Tries)
4. God(1 Try)""")
        difficulty = int(input())
        #EasyMode
        if difficulty == 1:
            print("Easy mode it is.")
            tries = 0
            while tries < 10:
                guess = int(input("Guess your number: "))
                if guess == number:
                    print(f"You won!. Good Game. You guessed in {tries} attempts.")
                    break
                if guess > number:
                    print("You are higher than the number. Try lower.")
                if guess < number:
                    print("You are lower than the number. Try higher.")
                tries += 1
                if tries == 10:
                    print(f"You failed. The number was {number}")
        #MediumMode
        elif difficulty == 2:
            print("Medium mode it is.")
            tries = 0
            while tries < 5:
                guess = int(input("Guess your number: "))
                if guess == number:
                    print(f"You won!. Good Game. You guessed in {tries} attempts.")
                    break
                if guess > number:
                    print("You are higher than the number. Try lower.")
                if guess < number:
                    print("You are lower than the number. Try higher.")
                tries += 1
                if tries == 5:
                    print(f"You failed. The number was {number}")
        #HardMode
        elif difficulty == 3:
            print("Hard mode it is.")
            tries = 0
            while tries < 3:
                guess = int(input("Guess your number: "))
                if guess == number:
                    print(f"You won!. Good Game. You guessed in {tries} attempts.")
                    break
                if guess > number:
                    print("You are higher than the number. Try lower.")
                if guess < number:
                    print("You are lower than the number. Try higher.")
                tries += 1
            if tries == 3:
                print(f"You failed. The number was {number}")
        #GodMode
        elif difficulty == 4:
            print("God tier it is.")
            tries = 0
            while tries < 1:
                guess = int(input("You got 1 chance. Guess your number: "))
                if guess == number:
                    print("You won!. True god.")
                    break
                if guess > number:
                    print("You are higher than the number. Try lower.")
                if guess < number:
                    print("You are lower than the number. Try higher.")
                tries += 1
                if tries == 1:
                    print(f"You failed. The number was {number}")
        #Rebound
        else:
            print("Enter a valid response.")
    
        print("Do you wanna play again?(y/n)")
        replay = input().lower()
        if replay == 'y':
            continue
        else:
            print("Thank you for playing. :)")
            break
    else:
        print("Thank you for checking out my game. :)")
        break


