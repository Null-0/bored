import random

num = random.randint(0,100)

user = input("what is the number between 1 and 100 I have picked? ")
userint = int(user)

if num == userint:
    print ("Great job! my number was ", num)
else:
    print ("incorrect my number was: ", num)