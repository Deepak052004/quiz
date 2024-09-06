print("Welcome to the quiz:")
interested=input("Are you interested!!")
score=0
if interested.lower()=="yes":
    print("Great!! Lets begin the game!!")
    Que1=input("What is the fullform of cpu: ")
    if Que1.lower()=="central processing unit":
        print("Correct Answer:")
        score+=1
    else:
        print("Wrong answer!! the correct answr is central procesing unit.")
    Que2=input("What is the full form of vs code?")
    if Que2.lower()=="virtual studio code ":
        print("correct answer!!")
        score+=1
    else:
        print("wrong answer!! correct answer is virtual studio code!!")
    Que3=input("What does ram stands for?")
    if Que3.lower()=="random access memory":
        print("correct answer!!")
        score+=1
    else:
        print("wrong answer!!,the correct answer is random access memory!!")

    print("the final score: ",score)
else:
    print("No problem!! Lets catchup soon")
