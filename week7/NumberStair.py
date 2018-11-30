"""NumberStair"""

def main(num):
    """main function"""
    count = 0
    line = 0
    for i in range(num):
        if line < count:
            print(i+1, end=' ')
            line += 1
        else:
            print(i+1)
            line = 0
            count += 1

main(int(input()))
