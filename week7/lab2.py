"""[Lab] Ascending Sort"""

def main(size):
    """main function"""
    empty = []
    for _ in range(size):
        empty.append(int(input()))
    empty.sort()
    print(empty[(x for x in range(len(empty)))])

main(int(input()))
