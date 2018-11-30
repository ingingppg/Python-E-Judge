"""Windmill"""
def main(step):
    """main function"""
    for i in range(1, step+1):
        print('*' * i + " "*(step-i) + "*" *(step-i+1) + " "*(i-1))
    for i in range(1, step+1):
        print(' '*(step-i) + "*"*i + ' '*(i-1) + '*'*(step-i+1))
main(int(input()))
