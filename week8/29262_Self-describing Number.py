"""Self-describing Number"""
def main():
    """Function Main"""
    numstr = input().strip('"')
    count = 0
    for i in range(len(numstr)):
        if i > 9:
            count += 1
            continue
        for j in numstr[i]:
            if numstr.count(str(i)) == int(j):
                count += 1
    if count == len(numstr):
        print("YES")
    else:
        print("NO")
main()
