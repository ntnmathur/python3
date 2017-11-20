def MovieTimes(tup_list):
    print("tup_list:", tup_list)
    sorted_list = sorted(tup_list, key = lambda x:x[0])
    print("tup_list sorted:", sorted_list)
    fnl_lst = []
    fnl_lst.append(tup_list[0])
    k=0
    i=1
    # 1 5 7 10
    # (1,3) (2,5) (3,4) (7,10)
    # -> (1,5) (3,4) (7,10)
    # --> (1,5) (7,10)
    while i < len(sorted_list):
        if sorted_list[i][0] < fnl_lst[k][1]:
            if sorted_list[i][1] < fnl_lst[k][1]:
                tmp = (fnl_lst[k][0], fnl_lst[k][1])
            else:
                tmp = (fnl_lst[k][0], sorted_list[i][1])
            del fnl_lst[k]
            fnl_lst.append(tmp)
        else:
            fnl_lst.append(sorted_list[i])
            k += 1
        i += 1
    print("final list merged:", fnl_lst)

    sum = 0
    for sublist in fnl_lst:
        sum = sum + (sublist[1] - sublist[0])

    return sum

if __name__ == "__main__":
    tup_list=[(0,15),(20,29),(40,50),(10,30),(45,54),(55,65)]
    print(MovieTimes(tup_list))