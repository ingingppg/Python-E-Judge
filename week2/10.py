"""10 - Determinant"""

def main():
    """main function"""
    numa = int(input())
    numb = int(input())
    numc = int(input())
    numd = int(input())
    nume = int(input())
    numf = int(input())
    numg = int(input())
    numh = int(input())
    numi = int(input())
    under_total = (numa * nume * numi) + (numb * numf * numg) + (numc * numd * numh)
    upper_total = (numg * nume * numc) + (numh * numf * numa) + (numi * numd * numb)
    print(under_total - upper_total)

main()
