"""Self-describing Number"""

def main(num):
    """main function"""
    num_1 = 0
    for i in range(len(num)):
        if num[i] == 0:
            num_1 = num.count('0')
        elif num[i] == 1:
            num_1 = num.count('1')
            

main(input())
