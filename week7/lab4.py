"""[Lab] Just Insert"""

def main(size):
    """main function"""
    empty = []
    for _ in range(size):
        empty.append(input())
    empty.insert(int(input()), input())
    print(empty)

main(int(input()))
