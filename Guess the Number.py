# import random module to generate random numbers
import random 

# generate a random target number between 1 and 100
target=random.randint(1, 100) 

# start a loop to allow user to guess until they get it right or choose to quit 
while True:
    user_choice=input("Guess the target or Quit:")
    if(user_choice=="Quit"):
        break

# convert user input to integer for comparison
    user_choice=int(user_choice)
    if(user_choice==target):
        print("successfully you guess the correct number")
        break
    elif(user_choice<target):
        print("your number is too small. Guess the bigger number...")
    else:
        print("your number is too big. Guess the smaller number...")


print("xxxxxGAME OVERxxxxx")


