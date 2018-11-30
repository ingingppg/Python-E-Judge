"""Jelly"""

def main(size):
    """main function"""
    time = 0
    size = [int(i) for i in size]
    while size != [1, 1, 1]:
        size.append(jelly(max(size)))
        size.remove(max(size))
        time += 1
    print(time)

def jelly(size):
    """cut jelly"""
    size = size//2
    return size

main(input().split(" "))
