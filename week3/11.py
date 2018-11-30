"""String Formatting"""

def main():
    """Main function"""
    name = input()
    price = int(input())
    weight = int(input())
    code = input()
    day = int(input())
    month = int(input())
    year = int(input())
    exp = int(input())
    print('Name:\t''%s' %name)
    print('Price:\t''%d' %price)
    print('Weight:\t''%d' %weight)
    print('ID:\t''%s' %code)
    print('EXP:\t''%02d/%02d/%d' %(day, month, year + exp))

main()
