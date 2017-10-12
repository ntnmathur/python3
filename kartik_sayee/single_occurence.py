import collections


def single_occurence(ary):

    d = collections.OrderedDict()
    for num in ary:
        if num in d:
            d[num] = d[num] + 1
        else:
            d[num] = 1

    return list(d.keys())


def single_occurence2(ary):
    fnl_lst = []
    for i in range(len(ary)):
        if ary[i] not in ary[:i]:
            fnl_lst.append(ary[i])
        else:
            continue
    return fnl_lst


if __name__ == "__main__":
    ary = [1, 2, 2, 7, 9, 4, 9, 4, 85, 6, 34, 6, 1, 10, 34, 45]
    a = single_occurence(ary)
    print(a)

    a = single_occurence2(ary)
    print(a)