"""Four Direction"""

def main(direction):
    """main function"""
    print(find(direction))

def find(direction):
    """return text direction"""
    line1, line2, line3, line4, line5 = '', '', '', '', ''
    direct = {"N":["  *  ", " *** ", "* * *", "  *  ", "  *  "], \
    "W":["  *  ", " *   ", "*****", " *   ", "  *  "], \
    "S":["  *  ", "  *  ", "* * *", " *** ", "  *  "], \
    "E":["  *  ", "   * ", "*****", "   * ", "  *  "]}
    for i in direction:
        if i in direct:
            line1 += direct[i][0] + ' '
            line2 += direct[i][1] + ' '
            line3 += direct[i][2] + ' '
            line4 += direct[i][3] + ' '
            line5 += direct[i][4] + ' '
        line = (line1 + '\n' + line2 + '\n' + line3 + '\n' + line4 + '\n' + line5)
    return line

main(input())
