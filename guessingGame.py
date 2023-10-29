import random
ranNum=random.randint(0,9)
##print(ranNum) This is to print the random number incase you want to see it
guess_count=0
guess_limit=3
while guess_count < guess_limit:
    guess=int(input("Guess:"))
    guess_count +=1
    if ranNum==guess:
     print("Congrats you won")
     break
    else:
       print("Wrong Guess!!Try Again")
    