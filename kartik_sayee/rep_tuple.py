def RepTup(lst,n):

    print(lst)
    out_lst=[]
    for i in lst:
        tmp_tup=tuple(i[:-1]+(n,))
        out_lst.append(tmp_tup)
    print(out_lst)


if __name__ == "__main__":
    lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    n=100
    RepTup(lst,n)