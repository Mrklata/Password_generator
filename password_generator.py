import random
import string


def main():
    length = int(input("length of password"))
    password = ''.join(random.choice(string.digits + string.ascii_letters)for _ in range(length))
    return password


print(main())
