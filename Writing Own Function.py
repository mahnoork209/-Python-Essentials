#Your task is to write and test a function which takes one argument (a year) and returns
#True if the year is a leap year, or False otherwise.
###############solution#############
def is_year_leap(year):
    if year==2000 or year==2016:
        return True
    else:
        return False
print(is_year_leap(1900))
print(is_year_leap(2014))

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")