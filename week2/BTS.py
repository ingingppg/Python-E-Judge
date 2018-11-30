"""5 - Flat rate"""

def main():
    """main function"""
    price = int(input())
    money = int(input())
    year = int(input())
    print(int((price - money) * (3.25/100)  * year))
    print(int(((price - money) + (((price - money) * (3.25/100)  * year)/(12 * year)))))

main()
