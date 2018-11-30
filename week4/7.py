"""Leap year"""

def main():
    """main function"""
    year = int(input())
    if year % 400 == 0:
        print("%s is a leap year." %year)
    elif year % 100 == 0:
        print("%s is not a leap year." %year)
    elif year % 4 == 0:
        print("%s is a leap year." %year)
    else:
        print("%s is not a leap year." %year)

main()
