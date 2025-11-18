print("Welcome to my quiz game!")

playing=input("Do you want to play? ")

# if playing !="yes" than quit the game
if playing != "yes":
    quit()

print("Okay, let's play :)")
score=0

answer=input("what does IDE stands for? ")
if answer=="integrated development environment":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

answer=input("what does GUI stands for? ")
if answer=="graphic user interface":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

print("You got " + str(score) + " question currect!")
print("You got " + str((score/2)*100) + "%.")