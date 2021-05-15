from random import *
from time import *

print("Welcome to Number Simulator!!!")
sleep(1)
print("In this game you have to find a random number by typing any number yourself and use the hints given after every attempt")
sleep(1)
print("If you want to play the game with limited number of tries, please press 1")
print("If you want to play the game with unlimited number of tries, please press 2")
sleep(1)
opt = int(input("Enter your choice here : "))
if(opt not in (1,2)):
    print("Invalid choice, please enter only 1 or 2")

elif(opt == 1):
    t = int(input("Enter the number of tries : "))
    num = randint(1,100)
    a = 1
    while(a <= t):
        n = int(input("Please enter a number : "))
        if(n >= 1 and n <= 100):
            if(n == num):
                sleep(1)
                print("Bingo!!!")
                print("You have guessed the number !!!")
                print(f"You took {a} tries to guess the number")
                break
            elif(n > num and a != t):
                print("Please enter a smaller number")
            elif(n < num and a != t):
                print("Please enter a larger number")
            elif(a == t):
                print("Uh oh, you have exhausted the number of tries")
        else:
            print("Please enter a number between 1 and 100 only")
        a = a + 1
    print(f"The number was {num}")
    if(n != num):
        print(f"You have failed to guess the number in {t} tries")

else:
    num = randint(1,100)
    a = 1
    while(a >= 1):
        n = int(input("Please enter a number : "))
        if(n >= 1 and n <= 100):
            if(n == num):
                sleep(1)
                print("Bingo!!!")
                print("You have guessed the number !!!")
                print(f"You took {a} tries to guess the number")
                break
            elif(n > num):
                print("Please enter a smaller number")
            elif(n < num):
                print("Please enter a larger number")
        else:
            print("Please enter a number between 1 and 100 only")
        a = a + 1
    print(f"The number was {num}")
