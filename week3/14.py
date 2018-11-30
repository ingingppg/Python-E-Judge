"""Time Machine"""

def main():
    """Main function"""
    month = input()
    destination = int(input())
    month12 = 'JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC'
    desmonth = month12.find(month)
    wooooo = (1 * desmonth + destination * 4)% 48
    print(month12[wooooo:wooooo+3])

main()
