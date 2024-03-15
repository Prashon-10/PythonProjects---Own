print("Welcome to my computer quiz!")

playing = input("Do you want to play the game? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does HTML stand for? ")
if answer.lower() == "hypertext markup language":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does CSS stand for? ")
if answer.lower() == "cascading style sheets":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does JPEG stand for? ")
if answer.lower() == "joint photographic experts group":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does DNS stand for? ")
if answer.lower() == "domain name system":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 7) * 100) + "%")