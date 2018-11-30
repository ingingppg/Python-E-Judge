"""X-Burner"""

def main():
    """main function"""
    empty = []
    slope = []
    while True:
        place = input()
        if place == 'Finish':
            break
        else:
            empty.append(place.split(','))
    for i in empty:
        if int(i[1]) > 0 and int(i[0]) > 0:
            slope.append(int(i[1])/int(i[0]))
            #Northeast++
        elif int(i[1]) < 0 and int(i[0]) > 0:
            slope.append(int(i[1])/int(i[0]))
            #Southeast+-
        elif int(i[0]) < 0 and int(i[1]) < 0:
            slope.append(int(i[1])/int(i[0]))
            #Southwest--
        elif int(i[1]) > 0 and int(i[0]) < 0:
            slope.append(int(i[1])/int(i[0]))
            #Northwest-+
        elif int(i[1]) > 0 and int(i[0]) == 0:
            #north
            slope.append('+')
        elif int(i[1]) == 0 and int(i[0]) > 0:
            #east
            slope.append(int(i[1])/int(i[0]))
        elif int(i[1]) < 0 and int(i[0]) == 0:
            #south
            slope.append('-')
        elif int(i[1]) == 0 and int(i[0]) < 0:
            #west
            slope.append(int(i[1])/int(i[0]))
    print(len(list(set(slope))))

main()
