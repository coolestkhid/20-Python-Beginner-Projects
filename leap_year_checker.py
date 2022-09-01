
from operator import is_
from traceback import print_tb


year = int(input("Enter a year: "))

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap Year")
            else:
                print("Not a Leap Year")
        else:
            print("Leap Year")
    else:
        print("Not Leap Year")
        
is_leap_year(year)