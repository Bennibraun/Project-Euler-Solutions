# Euler Problem 19

# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.

# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.

# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


sunday_count = 0
#0=monday, 6=sunday
weekday = 1
#1-31
date = 1
#0=jan, 11=dec
month = 0

year = 1901

def month_len(month, year):
    if month in [0,2,4,6,7,9,11]:
        return 31
    elif month in [3,5,8,10]:
        return 30
    elif month == 1:
        if year % 4 == 0:
            return 29
        else:
            return 28
    else:
        print('error in month_len(',month,',',year,')')
        return 0

len_m = month_len(month,year)

while(year < 2001):
    #check if new month started
    if date >= len_m:
        month += 1
        #check if new year started
        if month > 11:
            month = 0
            year += 1
        len_m = month_len(month,year)
        date = 0

    #check first sunday
    if weekday == 6 and date == 1:
        sunday_count += 1

    #next weekday
    weekday += 1
    if weekday > 6:
        weekday = 0

    date += 1


print(sunday_count)
print('date:',date)
print('weekday:',weekday)
print('month:',month)
print('year:',year)
