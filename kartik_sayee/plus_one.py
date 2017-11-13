def PlusOne(ary, n):
    i = len(ary) - 1
    fnl_num = []
    carry = 0
    while i >= 0:
        if i+1 == len(ary):
            val = ary[i] + n
        else:
            val = ary[i] + carry
        fnl_num.append(str(val%10))
        carry = int(val/10)
        i -= 1

    if carry != 0:
        fnl_num.append(str(carry))

    fnl_num.reverse()
    return ''.join(fnl_num)


if __name__ == "__main__":
    ary = [9, 9, 9, 7]
    n = 9
    print(PlusOne(ary, n))