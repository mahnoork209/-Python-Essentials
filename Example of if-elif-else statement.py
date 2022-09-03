#the following rule is used to determine the kind of year:
#if the year number isn't divisible by four, it's a common year;
#otherwise, if the year number isn't divisible by 100, it's a leap year;
#otherwise, if the year number isn't divisible by 400, it's a common year;
#otherwise, it's a leap year.


year = int(input("Enter a year: "))
if year%4!=0:
    print("Commom Year")
elif year%100!=0:
    print("Leap year")
elif year%400!=0:
    print("Common year")
else:
     print("Not within the Gregorian calendar period")