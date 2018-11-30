"""List the data"""

def main():
    """main function"""
    name = ''
    surname = ''
    nickname = ''
    age = ''
    for _ in range(10):
        text = input().split(' ')
        name += text[0] + ' '
        surname += text[1] + ' '
        nickname += text[2] + ' '
        age += text[3] + ' '
    print('list of name:', name)
    print('list of surname:', surname)
    print('list of nickname:', nickname)
    print('list of age:', age)
main()
