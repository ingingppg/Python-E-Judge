"""Super_Ultimate_Extreme_Month"""

def main():
    """Main function"""
    number = int(input())
    month = '1 January  2 February 3 March    4 April    5 May      6 June     \
    7 July     8 August   9 September10October  11November 12December'
    month_start = month.find(str(number)) + 1
    month_stop = month.find(str(number)) + 11
    print(month[month_start+1:month_stop])

main()
