"""[Midterm] Tax Calculator"""

def main(raw_tax):
    """main function"""
    if raw_tax * 12 > 100000:
        tax = (raw_tax*12) - 100000
    else:
        tax = raw_tax -(raw_tax * 12 * 0.5)
    if 0 <= tax <= 150000:
        print('0')
    elif 150001 <= tax <= 300000:
        print('%d' %((tax - 150000)*0.05))
    elif 300001 <= tax <= 500000:
        print('%d' %(((tax - 300000)*0.1)+ 7500))
    elif 500001 <= tax <= 750000:
        print('%d' %(((tax - 500000)*0.15)+27500))
    elif 750001 <= tax <= 1000000:
        print('%d' %(((tax - 750000)*0.2)+65000))
    elif 1000001 <= tax <= 2000000:
        print('%d' %(((tax - 1000000)*0.25)+115000))
    elif 2000001 <= tax <= 5000000:
        print('%d' %(((tax - 2000000)*0.3)+365000))
    elif tax > 5000000:
        print('%d' %(((tax - 5000000)*0.35)+1265000))

main(int(input()))
