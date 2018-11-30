"""Inverse Binary"""

def ing():
    """Main function"""
    number = input()
    inverse1 = number.replace('0', '2')
    inverse2 = inverse1.replace('1', '0')
    inverse3 = inverse2.replace('2', '1')
    print(inverse3)

ing()
