"""Sum of inverse string"""

def main():
    """Main function"""
    text_a1 = input()
    text_b1 = input()
    loca_a = int(input())
    loca_b = int(input())
    text_a2 = text_a1[::-1]
    text_b2 = text_b1[::-1]
    print(ord(text_a2[loca_a -1]) + ord(text_b2[loca_b -1]))

main()
