"""Tribonacci"""
import json
def main(lisst, position):
    """main function"""
    for i in range(position-3):
        lisst.append(lisst[i] + lisst[i+1] + lisst[i+2])
    print(lisst[:position])
main(json.loads(input()), int(input()))
