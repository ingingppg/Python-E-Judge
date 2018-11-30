"""Month"""

def main():
    """Main function"""
    number = int(input())
    month12 = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'
    month = (number * 4)
    print(month12[month-4:month-1])

main()
