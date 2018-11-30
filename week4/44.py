"""Taxi"""

def main():
    """main function"""
    distance = int(input())
    time = int(input())
    if distance > 65:
        price_taxi = 682.5 + (distance - 65) * 15
    elif 41 <= distance <= 65:
        price_taxi = 370 + (distance - 40) * 12.5
    elif 21 <= distance <= 40:
        price_taxi = 170 + (distance - 20) * 10
    elif 11 <= distance <= 20:
        price_taxi = 95 + (distance - 10) * 7.5
    elif 2 <= distance <= 10:
        price_taxi = 50 + (distance - 1) * 5
    elif 0 <= distance <= 1:
        price_taxi = 50
    price_taxi += (time // 60 + (time % 60 != 0)) * 1.5
    print(int(price_taxi) + (price_taxi % 1 != 0))

main()
