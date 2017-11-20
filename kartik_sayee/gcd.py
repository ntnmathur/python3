def GCD(ary):

    ary.sort()
    print(ary)
    sml_num = ary[0]
    big_num = ary[1]
    i=1
    while(i<len(ary)):
        big_num=ary[i]
        while big_num%sml_num!=0:
            rem=big_num%sml_num
            big_num=sml_num
            sml_num=rem
        i=i+1
    print(sml_num)

if __name__ == "__main__":
    ary = [54, 108, 144]
    GCD(ary)