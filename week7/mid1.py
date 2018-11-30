"""[Midterm] Exponentoal equation"""
import math
def main(number_x):
    """main function"""
    print(2 - number_x + (3/7)*(number_x**2) - (5/11)*(number_x**3) + math.log10(number_x))
main(float(input()))
