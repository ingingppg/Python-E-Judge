"""Super Dancer"""

def main(time):
    """main function"""
    for i in range(time):
        score = 0
        combo = 0
        number_note = int(input())
        note = input()
        hitnote = input()
        for i in range(number_note):
            if note[i] == hitnote[i]:
                combo += 1
                score += combo
            else:
                combo = 0
        print(score)

main(int(input()))
