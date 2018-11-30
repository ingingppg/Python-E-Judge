"""7 - Fat Donuts"""

def main():
    """main function"""
    radius_big = int(input())
    radius_small = int(input())
    print(int((3.1416 *(radius_big / 2) ** 2) - (3.1416 *(radius_small / 2) ** 2)))
    print(int((2 * 3.1416 *(radius_big / 2)) + (2 * 3.1416 *(radius_small / 2))))

main()
