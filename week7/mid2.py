"""[Midterm] Password generator"""

def password(username):
    """main function"""
    print((len(username) * (username[::-1] + '_'))[:-1])
password(input())
