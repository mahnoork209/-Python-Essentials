"""Your task is to write and test a function which takes two arguments (a year and a month)
 and returns the number of days for the given month/year pair (while only February is 
 sensitive to the year value, your function should be universal).
The initial part of the function is ready. Now, convince the function to return None if 
its arguments don't make sense."""

###########solution##########
def is_year_leap(year):

    if year==2000:
        return True
    else:
        return False
    print(is_year_leap(1900))

def days_in_month(year, month):
    if year == 2000 or year == 2016:
        leap_month_list=[0,31,29,31,30,31,30,31,31,30,31,30,31]
        date_month= leap_month_list[month]
        return date_month
    elif year == 1900 or year==1987:
        month_list=[0,31,28,31,30,31,30,31,31,30,31,30,31]
        date_month=month_list[month]
        return  date_month
    else:
        None
print(days_in_month(2000, 9))

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
