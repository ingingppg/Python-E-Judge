"""Caesar cipher"""

def main():
    """Main function"""
    text = input()
    cipher = ((ord(text) - 100) % 26 + 97)
    print(chr(cipher))

main()
