"""3 - Bank Notes"""

def main():
    """main function"""
    money = int(input())
    print(money//800)
    print(money%800//200)
    print(money%800%200//150)
    print(money%800%200%150//60)
    print(money%800%200%150%60//10)

main()
