def Intersection(ary1,ary2):
    final_lst = []
    if len(ary1) > len(ary2):
        big = ary1
        small = ary2
    else:
        big = ary2
        small = ary1

    for elem in big:
        if elem in small:
            final_lst.append(elem)

    print(final_lst)
    return final_lst


if __name__ == "__main__":
    ary1=[1, 2, 2, 1]
    ary2=[2, 2]

    Intersection(ary1,ary2)