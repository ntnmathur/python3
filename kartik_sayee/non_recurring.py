def NonRecur(ary):
    for i in range(len(ary)):
        elem = ary[i]
        if elem not in ary[i+1:]:
            return elem

if __name__ == "__main__":
    ary=[1,3,4,9,6,3,1,2,4,5,6,3,8]
    print(NonRecur(ary))
