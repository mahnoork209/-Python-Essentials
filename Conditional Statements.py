#using if statement
n=20
if i>10:
    print("HI!")
#using if statement by taking inputs
var=int(input("Enter first number:"))
if var<=100:
    print("Great Work:)")
#using if-else statment
i=10
if i<20 :
    print("Number is less") 
else:
    print("Number is greater")       
#using if-else by taking inputs
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))  
if num1>num2:
    print("First Number is greater!")
else:
    print("Second Number is greater")    
#using else-if statement
n1=int(input("Enter first number:"))

if n1>10:
    print(n1,"is greater than 10")
elif n1<10:
    print(n1,"is smaller than 10")
else:
    print("Number is equal!")
# find the largest of three numbers.
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

# We temporarily assume that the first number is larger
largest_number = n1

if n2 > largest_number:
    largest_number = n2

if n3 > largest_number:
    largest_number = n3

print("The largest number is:", largest_number)