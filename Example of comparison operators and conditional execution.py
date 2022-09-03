#Write a program that utilizes the concept of conditional execution, takes a string as input, and:
#.prints the sentence "Yes - Spathiphyllum is the best plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
#.prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
#.prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.

#Test Data
#Sample input: spathiphyllum
#Expected output: No, I want a big Spathiphyllum!
#Sample input: pelargonium
#Expected output: Spathiphyllum! Not pelargonium!
#Sample input: Spathiphyllum
#Expected output: Yes - Spathiphyllum is the best plant ever!

n1=str(input("Enter plant name:"))
n2=str("Spathiphyllum")
if n1==n2:
    print("\"Yes - Spathiphyllum is the best plant ever!\"")
if n1<=n2:
     print("\"No, I want a big Spathiphyllum!\"")
else:
    print("Spathiphyllum! Not",n1)
