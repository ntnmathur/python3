def MergeList(lst1,lst2):
    big_lst=[]
    sml_lst=[]
    fnl_lst=[]

    print(lst1)
    print(lst2)
    if len(lst1)>len(lst2):
        big_lst=lst1
        sml_lst=lst2
    else:
        big_lst=lst2
        sml_lst=lst1
    k=0
    i=0
    while(i<len(big_lst)):
        if k<len(sml_lst):
            if big_lst[i]<sml_lst[k]:
                fnl_lst.append(big_lst[i])
                i=i+1
            else:
                fnl_lst.append(sml_lst[k])
                k=k+1
        else:
            fnl_lst.append(big_lst[i])
            i=i+1

    print(fnl_lst)


if __name__ == "__main__":
    lst1 = [3, 4, 6, 10, 11, 18]
    lst2 = [1, 5, 7, 12, 13, 19, 21]
    MergeList(lst1,lst2)