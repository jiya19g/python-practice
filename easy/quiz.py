print("Welcome to my Quiz")
play=input("Do you want to play this game? ")

if play.lower()!="yes":
    quit

print("great!!")
score=0

answer=input("What does CPU stand for? ")
if answer.lower()=="central processing unit":
    score+=1
    print("Correct")
else:
    print("Incorrect")

answer=input("What does GPU stand for? ")
if answer.lower()=="graphics processing unit":
    score+=1
    print("Correct")
else:
    print("Incorrect")
    
answer=input("What does RAM stand for? ")
if answer.lower()=="random access memory":
    score+=1
    print("Correct")
else:
    print("Incorrect")

answer=input("What does PSU stand for? ")
if answer.lower()=="power supply unit":
    score+=1
    print("Correct")
else:
    print("Incorrect")
    
print("You got "+ str(score) +" as your score!")
print(score*100/4)