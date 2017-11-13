def Median(ary):
    l = len(ary)
    ary.sort()
    if l % 2 != 0:
        mid = int(l/2)
        return ary[mid]
    else:
        mid = int(l/2)
        mid_1 = int(l/2)+1
        return (ary[mid]+ary[mid_1])/2


if __name__ == "__main__":
    ary1 = [5, 89, 20, 64, 20, 45]
    print(Median(ary1))

    ary2 = [5, 89, 20, 64, 20, 45, 45, 23, 67, 32, 30]
    print(Median(ary2))