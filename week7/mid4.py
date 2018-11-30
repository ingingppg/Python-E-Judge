"""[Midterm] Cell phone bill"""

def main(bill):
    """main function"""
    phone_bill = bill.split(",")[0]
    message_bill = bill.split(",")[1]
    if int(phone_bill) <= 50 and int(message_bill) <= 50:
        print('Cell phone plan: $15.00')
        print('911 Call center support: $0.44')
        print('Total: $16.21')
    elif int(phone_bill) > 50 and int(message_bill) <= 50:
        total = 15 + ((int(phone_bill) - 50) * 0.25) + 0.44
        print('Cell phone plan: $15.00')
        print('Additional air time: $%.2f' %((int(phone_bill) - 50) * 0.25))
        print('911 Call center support: $0.44')
        print('Total: $%.2f' %(total * 0.05 + total))
    elif int(phone_bill) <= 50 and int(message_bill) > 50:
        total = 15 + ((int(message_bill) - 50) * 0.15) + 0.44
        print('Cell phone plan: $15.00')
        print('Additional text messages: $%.2f' %((int(message_bill) - 50) * 0.15))
        print('911 Call center support: $0.44')
        print('Total: $%.2f' %(total * 0.05 + total))
    elif int(phone_bill) > 50 and int(message_bill) > 50:
        total = (((15 +(int(phone_bill) - 50)* 0.25) + (int(message_bill)- 50)* 0.15)+ 0.44)
        print('Cell phone plan: $15.00')
        print('Additional air time: $%.2f' %((int(phone_bill) - 50) * 0.25))
        print('Additional text messages: $%.2f' %((int(message_bill) - 50) * 0.15))
        print('911 Call center support: $0.44')
        print('Total: $%.2f' %(total * 0.05 + total))
main(input())
