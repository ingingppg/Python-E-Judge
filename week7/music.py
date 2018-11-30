"""Music List"""

def main(name_song):
    """main function"""
    song = name_song.split(", ")
    song = check(song)
    song.sort(key=len, reverse=True)
    number = 1
    for i in song:
        if i != '0':
            print("%d.%s" %(number, i))
            number += 1

def check(song):
    """check duplicate song name"""
    for j in range(len(song)):
        for k in range(1, len(song)):
            if song[j].lower() == song[k].lower() and j != k:
                song[k] = '0'
    return song

main(input())
