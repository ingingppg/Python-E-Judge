""" Ez List อ่านให้จบนะ [List] """

def main(lissssssssssssss):
    """main function"""
    while True:
        aaa = int(input())
        if aaa != 0:
            lissssssssssssss.append(aaa)
        else:
            break
    print(lissssssssssssss)
    lissssssssssssss.sort()
    print(lissssssssssssss)
    lissssssssssssss.reverse()
    print(lissssssssssssss)
    print(lissssssssssssss.pop(2))
    print(lissssssssssssss)
    lissssssssssssss.clear()
    print(lissssssssssssss)

main(list())
