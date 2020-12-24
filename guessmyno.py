import random
number=random.randrange(1,10)
guess=int(input("guess a number between 1 and 10))
while guess!= number:
                if guess>number:
                     print("guess a lesser number.Try again")
                     guess=int(input("guess a number between 1 and 10))
                 else:
                     print("guess a higher number.Try again")
                     guess=int(input("guess a number between 1 and 10))
                                     
print("your guess is correct and You won the game")