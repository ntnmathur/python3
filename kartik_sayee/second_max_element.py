def second_max(ary):
    max = ary[0]
    sec_max = ary[0]
    for num in ary:
        if num > max:
            sec_max = max
            max = num
        elif num > sec_max:
            sec_max = num

    return sec_max

if __name__ == "__main__":
    ary = [5, 89, 20, 64, 20, 45, 53]
    i = second_max(ary)
    print(i)