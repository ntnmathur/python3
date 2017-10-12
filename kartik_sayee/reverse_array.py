def reverseary(ary1):
    reverse = []
    i = len(ary1)-1
    while i>=0:
        reverse.append(ary1[i])
        i -= 1
    return reverse


def reverseary_recursion(ary1):
    if len(ary1) == 0:
        return []
    else:
        return ary1[len(ary1)-1].extend(reverseary_recursion(ary1))


if __name__ == "__main__":
    ary1 = [1, 2, 3, 4, 5, 6, 7]
    print(ary1)
    a = reverseary(ary1)
    print(a)

    ary1 = [1, 2, 3, 4, 5, 6, 7]
    print(ary1)
    a = reverseary(ary1)
    print(a)