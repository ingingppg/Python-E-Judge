"""Count Vowel"""
 
def main(text, count):
    """main function"""
    print(check(text, count))
 
def check(text, count):
    """count vowel in str"""
    vowel = ['a', 'e', 'i', 'o', 'u']
    text = text.lower()
    for i in text:
        if i in vowel:
            count += 1
    return count
 
main(input(), 0)
