""" Print Lines [Loop] """

def main(line, alphabet):
    """main function"""
    for i in range(line):
        print("Line %d: " %(i+1), end="")
        for j in range(alphabet):
            print((j+1)%10, end="")
        print()

main(int(input()), int(input()))
