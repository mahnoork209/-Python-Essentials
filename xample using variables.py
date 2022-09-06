"""Your task is to:

1-create the variables: john, mary, and adam;
2-assign values to the variables. The values must be equal to the numbers of fruit possessed
 by John, Mary, and Adam respectively;
having stored the numbers in the variables, print the variables on one line, and separate 
each of them with a comma;
3-now create a new variable named total_apples equal to addition of the three former 
variables.
4-print the value stored in total_apples to the console;
experiment with your code: create new variables, assign different values to them,
 and perform various arithmetic operations on them (e.g., +, -, *, /, //, etc.). 
 5-Try to print a string and an integer together on one line, e.g., "Total number of apples:"
  and total_apples."""
############solution############
john = 3
mary = 5
adam = 6
print(john , mary , adam , sep=",")
total_apples =  john + mary + adam
print(total_apples)
print("Total number of Apples:",total_apples)