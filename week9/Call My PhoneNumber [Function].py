"""Call My PhoneNumber [Function]"""

def main(phonenum):
    """main function"""
    print(check(phonenum))

def check(number):
    """chage number to text"""
    text = ""
    number = number.replace('-', '')
    for i in number:
        if i == '0':
            text += 'zero '
        elif i == '1':
            text += 'one '
        elif i == '2':
            text += 'two '
        elif i == '3':
            text += 'three '
        elif i == '4':
            text += 'four '
        elif i == '5':
            text += 'five '
        elif i == '6':
            text += 'six '
        elif i == '7':
            text += 'seven '
        elif i == '8':
            text += 'eight '
        elif i == '9':
            text += 'nine '
    text = text[:-1]
    return text

main(input())
