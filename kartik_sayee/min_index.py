def MinIndex(ary1,ary2):

    min_idx=9999
    val=''

    for i in range(0,len(ary1)):
        key=ary1[i]
        if key in ary2:
            idx=i+ary2.index(key)
            if idx<min_idx:
                min_idx=idx
                val=ary1[i]

    print(val,min_idx)


if __name__ == "__main__":
    ary1=["Shogun", "Tapioca Express", "Burger King", "KFC"]
    ary2=["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    MinIndex(ary1,ary2)

    ary1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    ary2 = ["KFC", "Shogun", "Burger King"]
    MinIndex(ary1, ary2)