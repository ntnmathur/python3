def CntEleTup(lst):
    for i in range(len(lst)):
        if isinstance(lst[i], tuple):
            print(i)
            return i


if __name__ == "__main__":
    lst = [10, 20, 30, (10, 20), 40]
    CntEleTup(lst)