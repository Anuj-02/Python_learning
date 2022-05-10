import sys


def leap_date(year):
    leap = ''
    if year % 4 == 0 & year % 100 == 0:
        leap = True
    elif year % 100 == 0 & year % 400 == 0:
        leap = False
    return leap


try:
    year = int(input("Enter a year: "))
    leap_date(year)
except:
    print('Year should be in number')
    sys.exit(1)

if leap_date(year) == True:
    print(f"{year} is leap year")
else:
    print(f"{year} is not a leap year")
