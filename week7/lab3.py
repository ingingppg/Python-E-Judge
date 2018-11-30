"""[Lab] Join them"""

def main(size):
    """main function"""
    empty = []
    for _ in range(size):
        empty.append(input())
    print(input().join(empty))

main(int(input()))
