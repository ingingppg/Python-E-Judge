"""Caesar Cipher Again!"""

def main():
    """main function"""
    text = input()
    if 65 <= ord(text) <= 90 or 97 <= ord(text) <= 122:
        if ord(text) >= 68 and ord(text) <= 90:
            print(chr(ord(text) -3))
        elif ord(text) >= 100 and ord(text) <= 122:
            print(chr(ord(text) -3))
        elif ord(text) == ord('A'):
            print("X")
        elif ord(text) == ord('B'):
            print("Y")
        elif ord(text) == ord('C'):
            print("Z")
        elif ord(text) == ord('a'):
            print("x")
        elif ord(text) == ord('b'):
            print("y")
        elif ord(text) == ord('c'):
            print("z")
    else:
        print(text)

main()
