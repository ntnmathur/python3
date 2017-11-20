def Dissapered(ary):
    lst = []
    start = min(ary)
    end = max(ary)

    elem = start
    while elem <= end:
        if elem not in ary:
            lst.append(elem)
        elem = elem + 1
    print(lst)
    return lst

if __name__ == "__main__":
    ary=[4,3,2,7,8,2,3,1]
    Dissapered(ary)