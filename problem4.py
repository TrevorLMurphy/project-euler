def find_largest_palindrome():
    """Find largest palindrome from multiplying
    two 3 digit numbers"""
    num_first = 999
    num_second = 999
    num_str = str(999 * 999)
    palindrome_list = []
    while num_first > 100:
        while num_second > 100:
            if num_str == num_str[::-1]:
                palindrome_list.append(int(num_str))
            num_second -= 1
            num_str = str(num_first * num_second)
        num_first-=1
        num_second = num_first # Prevent duplicate comparisons
    return max(palindrome_list)


if __name__ == '__main__':
    print find_largest_palindrome()
