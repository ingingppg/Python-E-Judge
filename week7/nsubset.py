"""[Lab] nSubset"""

def main(text):
    """main function"""
    numcheck = 0
    num = 0
    count = 0
    if text == '{}':
        print('1')
    else:
        for i in text:
            numcheck += 1
            if i == "," and num == 0:
                count += 1
            if i == "{" and numcheck > 1:
                num += 1
            if i == "}":
                num -= 1
        print(2**(count+1))
main(input())
