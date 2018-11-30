"""Taxi"""

def main():
    """main function"""
    distance = int(input())
    time = int(input())
    if distance > 65:
        print(round((682.5 + (distance - 65) * 15) + (1.5 * (round(time/60)))))
    elif 41 <= distance <= 65:
        print(round((370 + (distance - 40) * 12.5) + (1.5 * (round(time/60)))))
    elif 21 <= distance <= 40:
        print(round((170 + (distance - 20) * 10) + (1.5 * (round(time/60)))))
    elif 11 <= distance <= 20:
        print(round((95 + (distance - 10) * 7.5) + (1.5 * (round(time/60)))))
    elif 2 <= distance <= 10:
        print(round((50 + (distance - 1) * 5) + (1.5 * (round(time/60)))))
    elif 0 <= distance <= 1:
        print(round(50 + (1.5 * (round(time/60)))))
main()
 