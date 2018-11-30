"""Password 2.0"""
def main():
    """Function Main"""
    pasw = input()
    score = 0
    if len(pasw) < 6:
        print("try again")
        pasw = input()
        if len(pasw) < 6:
            print("process terminated")
    if len(pasw) >= 6:
        if pasw.isnumeric():
            score += 50
        elif pasw.isalpha():
            score += 30
            if pasw.islower():
                score += 100
            elif pasw.isupper():
                score += 85
            elif pasw.isalpha():
                score += 175
        elif pasw.isalnum():
            score += 75
        repeated = pasw.count(pasw[0])-1
        if repeated > 3:
            score -= (repeated-3)*15
        if len(pasw) > 10:
            score += (len(pasw)-10)*10
        score += ord(pasw[-1])
        print("Password :", "*"*len(pasw))
        print("Security score :", score)
        level = "poor"*bool(score < 150) + "acceptable"*bool(150 <= score < 300) + \
                "secure"*bool(score >= 300)
        print("Security level : {0}".format(level))
main()
