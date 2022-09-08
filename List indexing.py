"""Your task is to write a program which removes all the number repetitions from the list.
 The goal is to have a list in which all the numbers appear not more than once."""

###############solution###################
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list=my_list[2:9]
for i in my_list:
    if i in new_list:
       del my_list[i]
print("The list with unique elements only:")
print(my_list)