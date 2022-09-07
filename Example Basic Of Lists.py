"""write a line of code that prompts the user to replace the middle number in the list
 with an integer number entered by the user (Step 1)
write a line of code that removes the last element from the list (Step 2)
write a line of code that prints the length of the existing list (Step 3)."""
##############solution##########
hat_list=[1,2,3,4,5]
hat_list[2]=int(input("Enter a number to replace with middle number:"))
del hat_list[4]
print("Length of the existing list=",len(hat_list))
print(hat_list)
