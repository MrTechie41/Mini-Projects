print("----- Welcome to the quiz! -----")

playing = input("Do you want to play (yes/no)? ")

if playing.lower() != "yes":
    quit()

print("Let's play then :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("-- Correct! --")
    score += 1
else:
    print("-- Incorrect! --")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("-- Correct! --")
    score += 1
else:
    print("-- Incorrect! --")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("-- Correct! --")
    score += 1
else:
    print("-- Incorrect! --")

answer = input("What does PSU stands for? ")
if answer.lower() == "power supply":
    print("-- Correct! --")
    score += 1
else:
    print("-- Incorrect! --")

answer = input("What does TCP stands for? ")
if answer.lower() == "transmission control protocol":
    print("-- Correct! --")
    score += 1
else:
    print("-- Incorrect! --")

print("You got " + str(score) + " questions correct!")

print("You got " + str((score / 5) * 100) + " %.")

print("----- Game Over -----")