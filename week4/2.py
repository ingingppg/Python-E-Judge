"""Grade(No If_Else)"""

def main():
    """main function"""
    score = int(input())
    grade = (bool(0 <= score <= 49) * "0") +\
    (bool(50 <= score <= 54) * "1") +\
    (bool(55 <= score <= 59) * "1.5") +\
    (bool(60 <= score <= 64) * "2") +\
    (bool(65 <= score <= 69) * "2.5") +\
    (bool(70 <= score <= 74) * "3") +\
    (bool(75 <= score <= 79) * "3.5") +\
    (bool(80 <= score <= 100) * "4") +\
    (bool(score < 0 or score > 100) * "Invalid")
    print(grade)

main()
