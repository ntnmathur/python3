def CountList(lst):
    out_lst = []
    for elem in lst:
        if isinstance(elem, list):
            out_lst.extend(CountList(elem))
        else:
            out_lst.append(elem)
    return out_lst


def CountTup(lst):
    out_lst = []
    for elem in lst:
        if isinstance(elem, (tuple, list)):
            out_lst.extend(CountTup(elem))
        else:
            out_lst.append(elem)
    return out_lst


if __name__ == "__main__":
    lst=[1,2,[1,2,3,[3,3],[5,6,7]],4,5,6,[7,6,4],[8,7,4,5,[6,7,8]]]
    print(lst)
    print(CountList(lst))
    tup = (1, 2, (1, 2, 3, (3, 3), [5, 6, 7]), 4, 5, 6, (7, 6, 4), (8, 7, 4, 5, (6, 7, 8)))
    print(tup)
    print(CountTup(tup))