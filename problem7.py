def is_prime(n):
    """Naive Primality Test"""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == '__main__':
    count = 1
    num = 1
    while count < 10001:
        num += 2
        if is_prime(num): count+=1
    print 'The 10001th prime number is {}'.format(num)
