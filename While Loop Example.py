"""will ask the user to enter an integer number;
will use a while loop;
will check whether the number entered by the user is the same as the number picked by the 
magician. If the number chosen by the user is different than the magician's secret number,
the user should see the message "Ha ha! You're stuck in my loop!" and be prompted to enter
a number again. If the number entered by the user matches the number picked by the
magician, the number should be printed to the screen, and the magician should say the
 following words: "Well done, muggle! You are free now."""

secret_number=97
print("Welcome to my game, muggle!")
number=int(input("Enter an integar:"))
while number!=0:
    if number!=secret_number:
           print(" \"Ha ha! You\'re stuck in my loop!\" ")
           number=int(input("Enter an integar again:"))  
    else:
        print("The Secret Number is:",number)
        print("\"Well done, muggle! You are free now.\"")
        break #for breaking loop