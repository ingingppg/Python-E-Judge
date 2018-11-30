"""Autocorrect 1.0"""

def main(num):
    """main function"""
    if 'Z' in num.upper():
        print('0')
    elif 'O' in num.upper() and 'N' in num.upper():
        print('1')
    elif 'W' in num.upper() and 'T' in num.upper():
        print('2')
    elif 'H' in num.upper() and 'R' in num.upper() and 'T' in num.upper():
        print('3')
    elif 'U' in num.upper() and 'O' in num.upper():
        print('4')
    elif 'F' in num.upper() and 'V' in num.upper():
        print('5')
    elif 'X' in num.upper():
        print('6')
    elif 'V' in num.upper() and 'S' in num.upper() and 'N' in num.upper():
        print('7')
    elif 'G' in num.upper()  and 'I' in num.upper() and 'H' in num.upper():
        print('8')
    elif 'N' in num.upper() and 'E' in num.upper() and 'I' in num.upper():
        print('9')
main(input())
