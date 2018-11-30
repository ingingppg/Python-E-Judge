""" Magic Function [Loop] """

def main(xxx):
    """main function"""
    while xxx > 1:
        if xxx % 2 == 0:
            print(xxx//2)
            xxx = xxx//2
        else:
            print(xxx+1)
            xxx = xxx+1
main(int(input()))
