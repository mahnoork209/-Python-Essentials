"""Your task is to complete the code in order to evaluate the following expression:

3x3 - 2x2 + 3x - 1

The result should be assigned to y."""
##############solution############
x = 0 #try other numbers by changing 0 
x = float(x)
y= (3 * x ** 3) - (2 * x **2) + (3 * x) -1
print("y =", y)

"""Your task is to prepare a simple code able to evaluate the end time of a period of time,
 given as a number of minutes (it could be arbitrarily large). The start time is given 
 as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the
 console.
For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16."""
###########solution#########
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

minutes = ( mins + dura ) % 60
hours= int(hour + (mins + dura) / 60) % 24
print(hours,minutes,sep=":")
