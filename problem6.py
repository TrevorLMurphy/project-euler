def sum_of_squares(lyst):
    return sum([x**2 for x in lyst])

def square_of_sums(lyst):
    return sum(lyst)**2

if __name__ == '__main__':
    hundred_nums = list(range(1,101))
    sums = sum_of_squares(hundred_nums)
    squares = square_of_sums(hundred_nums)
    print 'Sum of squares is {}'.format(sums)
    print 'Square of sums is {}'.format(squares)
    print 'Difference is {}'.format(squares-sums)
