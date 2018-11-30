""" N to M [Loop] """

def main(nnn, mmm):
    """main function"""
    if nnn > mmm:
        for i in range(nnn, mmm-1, -1):
            print(i, end=" ")
    elif mmm > nnn:
        for i in range(nnn, mmm+1):
            print(i, end=" ")
    else:
        print(nnn)

main(int(input()), int(input()))
