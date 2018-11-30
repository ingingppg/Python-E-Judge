"""Text Justify Right"""

def main():
    """Main function"""
    text = input()
    size = int(input())
    print("{0:>{1}}".format(text, size))

main()
