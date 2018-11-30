"""Prime Number [Function] """
 
def main(number):
    """main function"""
    print(is_prime(number))
 
def is_prime(num):
    """check number is prime"""
    if num >= 2:
        for i in range(2, int((num**0.5)+1)):
            if num%i == 0:
                return 'No'
        return 'Yes'
    return 'No'
 
main(int(input()))