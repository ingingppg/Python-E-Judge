"""GCD"""

def main(aaa, bbb):
    """main function"""
    hcf_x_lcm = aaa * bbb
    if aaa == 0 or bbb == 0:
        hcf, lcm = 0, 0
    else:
        hcf = 1
        for i in range(1, hcf_x_lcm+1):
            if aaa%i == 0 and bbb%i == 0:
                aaa = aaa/i
                bbb = bbb/i
                hcf *= i
        lcm = hcf_x_lcm//hcf
    print(hcf)
    print(lcm)
main(int(input()), int(input()))
