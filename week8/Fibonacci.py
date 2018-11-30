"""Fibonacci"""

def main(position):
    """main function"""
    fn1 = 0
    fn2 = 1
    fnn = 0
    fibo = [0, 1]
    if position == 0:
        print(fibo[0])
    elif position == 1:
        print(fibo[1])
    else:
        for _ in range(position-1):
            fnn = fn1 + fn2
            fn1 = fn2
            fn2 = fnn
            fibo.append(fnn)
        print(fibo[position])

main(int(input()))
