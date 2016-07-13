# stackoverflow.com/questions/23287/largest-prime-factor-of-a-number

def largest_prime(n):
    d = 2
    while n > 1:
        while n % d == 0:
            n /= d
        d += 1
        if d * d > n and n > 1: # Reduces the algorithm to O(sqrt(n))
            break
    return n

if __name__ == '__main__':
    num = 600851475143
    print largest_prime(num)
