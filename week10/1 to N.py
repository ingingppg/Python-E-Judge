""" 1 to N [Loop] """

def main(nnn, step, count):
    """main function"""
    while count < nnn:
        print('%.1f' %count, end=" ")
        count += step

main(int(input()), float(input()), 1)
