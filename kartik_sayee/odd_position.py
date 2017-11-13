def OddPosition(ary):
    fnl_list = []
    for elem in ary:
        if elem%2 !=0:
            fnl_list.append(elem)
    return fnl_list

if __name__ == "__main__":
    ary = [0, 1, 2, 3, 4, 5]
    print(OddPosition(ary))