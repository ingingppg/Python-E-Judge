"""Count vowel"""

def main():
    """Main function"""
    text = input()
    big_a = text.count('A')
    big_e = text.count('E')
    big_i = text.count('I')
    big_o = text.count('O')
    big_u = text.count('U')
    small_a = text.count('a')
    small_e = text.count('e')
    small_i = text.count('i')
    small_o = text.count('o')
    small_u = text.count('u')
    print(big_a + big_e + big_i + big_o + big_u + small_a + small_e + small_i + small_o + small_u)

main()
