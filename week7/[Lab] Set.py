"""[Lab] Set"""
def main(text1, text2):
    """Main"""
    if text1 == "{}" and text2 == "{}":
        print("set()")
        print("set()")
    elif text2 == "{}":
        seta = list(map(int, text1[1:-1].split(",")))
        seta.sort()
        print(set(seta))
        print("set()")
    elif text1 == "{}":
        setb = list(map(int, text2[1:-1].split(",")))
        setb.sort()
        print(set(setb))
        print("set()")
    else:
        seta = list(map(int, text1[1:-1].split(",")))
        setb = list(map(int, text2[1:-1].split(",")))
        #print(set(seta) | set(setb))
        print(set(seta).union(set(setb)))
        print(set(seta).intersection(set(setb)))
        #print(set(seta) & set(setb))
main(input(), input())
