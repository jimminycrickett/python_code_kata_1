from random import randint

Name = input("What's your name?\n")
My_Number = int(randint(0,11))
Count = int(1)
Guesses = []
Test_Number = input("Hello " + Name + "please pick a the secret number between 1 and 10: ")
Test_Number = int(Test_Number)
while(1):
    if(6 == Count):
        print("Guess you're just not that lucky...")
        quit()
    print("You've made " + str(Count) + " attempts")
    print("Your number is " + str(Test_Number))
    if(Test_Number != My_Number):
        if(Test_Number in Guesses):
            print("You already tried that, dumbass...")
        else:
            Guesses.append(Test_Number)
        print("Attempted Guesses so far: " + str(Guesses))
        Count = Count + 1
        print("HA! wrong...")
        Test_Number = input("Try again: ")
        Test_Number = int(Test_Number)
    else:
        print("... lucky bitch.")
        quit()
    # If my_number is smaller than 100 at this point, loop again
