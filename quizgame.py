Welcome= input("welcome to The Quiz, Type yes to begin: ")
if Welcome == "yes":
    print("ok lets begin")
Q1 = input("what is 3x5+20? ")
if Q1 == "35":
    print("correct!")

    Q2 = input("what is 3x5*20? ")
    if Q2 == "300":
        print("correct!")

        Q3 = input("what is 3x5*2-15? ")
        if Q3 == "15":
            print("correct!")
        name = input("You won the game enter name to win certificate: ")
        print("Good Job "+name)
else:
    quit()
