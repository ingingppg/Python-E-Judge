"""9 - Quadratic equation"""

def main():
    """main function"""
    numa = int(input())
    numb = int(input())
    numc = int(input())
    total = ((numb**2) - 4 * numa * numc)
    positive = ((-numb + (total**(1/2))) / (2 * numa))
    negative = ((-numb - (total**(1/2))) / (2 * numa))
    print("%.2f" %(positive + negative))
main()
