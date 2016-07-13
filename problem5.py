def smallest_multiple():
    num_list = list(range(1,21))
    i = num_list[-1]
    while True:
        not_divisible = False
        for num in num_list:
            if i % num != 0:
                not_divisible = True
        if not_divisible is False:
            return i
        i += 20


if __name__ == '__main__':
    print smallest_multiple()
