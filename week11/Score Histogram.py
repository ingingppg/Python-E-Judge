"""Score Histogram"""
 
def main(score, check):
    """main function"""
    #check repeat var
    score = [int(i) for i in score]
    for j in score:
        if j not in check:
            check.append(j)
    for k in check:
        if 0 <= k <= 1:
            print('0-1:%s' %('|'*(score.count(k))))
        elif 1 < k <= 2:
            print('1-2:%s' %('|'*(score.count(k))))
        elif 2 < k <= 3:
            print('2-3:%s' %('|'*(score.count(k))))
        elif 3 < k <= 4:
            print('3-4:%s' %('|'*(score.count(k))))
        elif 4 < k <= 5:
            print('4-5:%s' %('|'*(score.count(k))))
        elif 5 < k <= 6:
            print('5-6:%s' %('|'*(score.count(k))))
        elif 6 < k <= 7:
            print('6-7:%s' %('|'*(score.count(k))))
        elif 7 < k <= 8:
            print('7-8:%s' %('|'*(score.count(k))))
        elif 8 < k <= 9:
            print('8-9:%s' %('|'*(score.count(k))))
        elif 9 < k <= 10:
            print('9-10:%s' %('|'*(score.count(k))))
    
main(input().split(","), [])
