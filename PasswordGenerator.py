import random
import string

if __name__ == 'main':
    total = string.ascii_letters + string.digits + string.punctuation
    length = 16
    password = "".join(random.sample(total, length))
    print(password)