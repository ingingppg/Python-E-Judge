"""Overlapping"""

def main():
    """main function"""
    xx1 = float(input())
    yy1 = float(input())
    radius1 = float(input())
    xx2 = float(input())
    yy2 = float(input())
    radius2 = float(input())
    x12y12 = (((xx2 - xx1)**2) + ((yy2 - yy1)**2))**(1/2)
    if (radius1 + radius2) >= x12y12:
        print("Yes")
    else:
        print("No")

main()
