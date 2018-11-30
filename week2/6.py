"""6 - Distance"""

def main():
    """main function"""
    kid1 = int(input())
    kid2 = int(input())
    benny1 = int(input())
    nutchy2 = int(input())
    bank1 = int(input())
    hun2 = int(input())
    d01 = (((benny1 - kid1)** 2) + ((nutchy2 - kid2)** 2)) ** (1/2)
    d02 = (((bank1 - benny1)** 2) + ((hun2 - nutchy2)** 2)) ** (1/2)
    print("%.2f" %(d01 + d02))

main()
