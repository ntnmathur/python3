def MovingZero(ary):

    # for i in range(0,len(ary)):
    #     if ary[i]==0:
    #         ary.append(0)
    #         del ary[i]
    # print(ary)
    lst = []
    count_zeros = 0
    for elem in ary:
        if elem == 0:
            count_zeros += 1
        else:
            lst.append(elem)

    for i in range(count_zeros):
        lst.append(0)

    print(lst)
    return lst

if __name__ == "__main__":
    ary=[0, 1, 0, 3, 12]
    MovingZero(ary)