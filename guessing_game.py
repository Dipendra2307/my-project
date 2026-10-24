import random
guess=0
count=0
difficulty=input("Enter the difficulty you want(EASY,MEDIUM,HARD):")
if difficulty.lower() == "easy":
        number=random.randint(1,50)
        while(number != guess):
            guess = int(input("Enter a number to be guessed between 1 to 50 :"))
            if number == guess:
                count+=1
                print("congratulation! you found the number in",count,"steps ")
            elif number > guess:
                count+=1
                print("Sorry you enter smaller number ")
            elif number< guess:
                count+=1
                print("Sorry you enter larger number ")
if difficulty.lower() == "medium":
        number=random.randint(1,100)
        while(number != guess):
            guess = int(input("Enter a number to be guessed between 1 to 100 :"))
            if number == guess:
                count+=1
                print("congratulation! you found the number in",count,"steps ")
            elif number > guess:
                count+=1
                print("Sorry you enter smaller number ")
            elif number< guess:
                count+=1
                print("Sorry you enter larger number ")
if difficulty.lower() == "hard":
        number=random.randint(1,500)
        while(number != guess):
            guess = int(input("Enter a number to be guessed between 1 to 500 :"))
            if number == guess:
                count+=1
                print("congratulation! you found the number in",count,"steps ")
            elif number > guess:
                count+=1
                print("Sorry you enter smaller number ")
            elif number< guess:
                count+=1
                print("Sorry you enter larger number ")