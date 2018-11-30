"""[Midterm] Lottery"""

def main():
    """main function"""
    onenum = input()
    twoendnum = input()
    threeendnum = input()
    first = input()
    last = input()
    prize = 0
    for i in range(int(first), int(last)):
        if i == onenum:
            prize += 10000
    for j in range(int(first[3:]), int(last[3:])):
        if j == twoendnum:
            prize += 25
    for k in range(int(first[2:]), int(last[2:])):
        if k == threeendnum:
            prize += 100
    print(prize)
main() 