"""Overlapping Clock Hands"""

def main():
    """main function"""
    time = input()
    hour, minu = time.split()
    hhh = int(hour)%12*5+int(minu)/12
    mmm = int(minu)
    total = bool(hhh >= mmm and abs(hhh-mmm) < 2)
    print(total)
    
main()
