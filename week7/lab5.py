"""[Lab] Set"""

def main(seeta, seetb):
    """main function"""
    aaa = ''
    bbb = ''
    if seeta == '{}' and seetb == '{}':
        print(set())
        print(set())
    elif seeta == '{}' and seetb != '{}':
        print(seetb)
        print(seetb)
    elif seeta != '{}' and seetb == '{}':
        print(seeta)
        print(seeta)
    else:
        aaa = seeta[1:-1].split(',')
        bbb = seetb[1:-1].split(',')
        aaa.extend(bbb)
    int(aaa)
    aaa.sort()
    print(aaa)
main(input(), input())
