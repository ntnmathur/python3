def cumulativeSum(ary):
    fnl_ary = []
    sum = 0
    for i in range(len(ary)):
        fnl_ary.append(sum + ary[i])
        sum += ary[i]
    print(fnl_ary)


if __name__ == "__main__":
    ary = [1, 1, 1]
    cumulativeSum(ary)

    ary = [1, -1, 3]
    cumulativeSum(ary)