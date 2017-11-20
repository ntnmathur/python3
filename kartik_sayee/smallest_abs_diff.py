def SmlAbsDiff(ary):
    print(ary)
    sorted_ary = sorted(ary)
    print(sorted_ary)

    min_diff = max(sorted_ary) # or some high value
    for i in range(1, len(sorted_ary)):
        diff = sorted_ary[i] - sorted_ary[i-1]
        if min_diff > diff:
            min_diff = diff
    print(min_diff)
    return min_diff

if __name__ == "__main__":
    ary=[30,15,21,17,24,5]
    SmlAbsDiff(ary)

    ary = [1, -2, 3, -4, 4, -5]
    SmlAbsDiff(ary)

    ary = [1,2,3,4,4,5]
    SmlAbsDiff(ary)