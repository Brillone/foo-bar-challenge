def get_code(l, l_sum, possible_remainders):
    # get remainder
    remainder = l_sum % 3

    # finish condition
    if remainder == 0:
        return build_code(l)
    
    if remainder in possible_remainders:
        # remainder was not checked (exact solution)
        target_remainder = remainder
        # remove exact solution possibility
        possible_remainders = [r for r in possible_remainders if r!=remainder]
    else:
        # no exact solution try from possiblities remained
        target_remainder = possible_remainders.pop()
    
    # loop elements
    for ix in range(len(l)):
        l_new_sum = l_sum - l[-ix-1]
        element_remainder = l[-ix-1] % 3

        # found element with target remainder
        if element_remainder == target_remainder:
            l.pop(-ix-1)

            return get_code(l=l, l_sum=l_new_sum, possible_remainders=possible_remainders)

    # test more remainders (happens when no exact solution)
    if len(possible_remainders) > 0:
        return get_code(l=l, l_sum=l_sum, possible_remainders=possible_remainders)

    # out of options
    return get_code([], 0, [])


def build_code(l):
    return sum([l[-i-1]*(10**i) for i in range(len(l))])


def solution(l):
    # init
    l_sum = sum(l)
    possible_remainders = [1, 1, 2, 2]

    # sort reversed
    l.sort(reverse=True)

    # get code 
    code = get_code(l, l_sum, possible_remainders)

    return code


if __name__ == "__main__":
    assert solution([3, 1, 4, 1]) == 4311
    assert solution([3, 1, 4, 1, 5, 9])) == 94311
