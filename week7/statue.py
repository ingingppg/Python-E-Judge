"""Statue"""
def main(line):
    """main function"""
    empty = []
    qaurter1 = []
    qaurter2 = []
    qaurter3 = []
    qaurter4 = []
    for _ in range(line):
        empty.append(input().split(','))
    for i in empty:
        if int(i[1]) > 0 and int(i[0]) > 0:
            qaurter2.append(int(i[1])/int(i[0]))
            #Northeast++
        elif int(i[1]) < 0 and int(i[0]) > 0:
            qaurter3.append(int(i[1])/int(i[0]))
            #Southeast+-
        elif int(i[0]) < 0 and int(i[1]) < 0:
            qaurter4.append(int(i[1])/int(i[0]))
            #Southwest--
        elif int(i[1]) > 0 and int(i[0]) < 0:
            qaurter1.append(int(i[1])/int(i[0]))
            #Northwest-+
        elif int(i[1]) > 0 and int(i[0]) == 0:
            #north
            qaurter1.append('+')
        elif int(i[1]) == 0 and int(i[0]) > 0:
            #east
            qaurter2.append(int(i[1])/int(i[0]))
        elif int(i[1]) < 0 and int(i[0]) == 0:
            #south
            qaurter3.append('-')
        elif int(i[1]) == 0 and int(i[0]) < 0:
            #west
            qaurter4.append(int(i[1])/int(i[0]))
    print(len(list(set(qaurter1))) + len(list(set(qaurter2))) \
    + len(list(set(qaurter3))) + len(list(set(qaurter4))))
main(int(input()))
