"""[Lab] nSubset"""

def main(supset):
    """main function"""
    if supset == '{}':
        print("1")
    else:
        print(2**len(supset[1:-1].split(",")))

main(input())
