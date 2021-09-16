import random
import string


def Random_Password_Generator():
    ans = ' '
    for i in range(1,11):
        if i%3 == 0:
            ans = ans + random.choice(string.digits)
        else:
            ans = ans + random.choice(string.ascii_letters)
    return ans
print(Random_Password_Generator())
