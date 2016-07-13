if __name__ == '__main__':
    prev_i = 1
    i = 2
    even_sum = 0
    while i < 4000000:
        if i % 2 == 0:
            even_sum += i
        temp = i
        i += prev_i
        prev_i = temp
    print even_sum
