def checkio(N):
    """ clear res, answer values
    """

    res = []
    answer = ""
    return base(N, res, answer)


def base(n, res=[], answer = ""):
    """
    find diviers in range [2--9]
    if dividers not found return 0
    """

    ii = 0
    for i in range(2,10):
        if ii != n:
            if n % i == 0:
                ii = i

    if ii != 0:
        n = n // ii
        res.append(ii)

        return base(n, res)
    if n < 9:
        for i in sorted(res):
            answer += str(i)
        return int(answer)
    else:
        return 0



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
    print("OK")
