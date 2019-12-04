def first_task():
    return sum([check(i) for i in range(125730, 579381)])

def second_task():
    return sum([check_harder(i) for i in range(125730, 579381)])

def check(number):
    number = str(number)
    got_double = False
    for i, e in enumerate(number[1:]):
        if number[i] > e:
            return False
        elif number[i] == e:
            got_double = True

    return got_double


def check_harder(number):
    if check(number):
        number = str(number)
        count_of_numbers = [number.count(i) for i in number]
        """
        the two adjacent matching digits are not part of a larger group of matching digits
        => at least, there exists one tuple of digits of size 2
        """
        return 2 in count_of_numbers
    else:
        return False

if __name__ == "__main__":
    assert check(111111) is True
    assert check(223450) is False
    assert check(123789) is False
    print("first_task: ", first_task())


    assert check_harder(112233) is True
    assert check_harder(123444) is False
    assert check_harder(111122) is True
    print("second_task: ", second_task())
