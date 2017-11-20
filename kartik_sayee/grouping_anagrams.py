def GroupingAnagrams(lst):
    dict={}
    print(lst)
    for i in lst:
        key=i
        tmp_key=''.join(sorted(key))
        if tmp_key in dict:
            dict[tmp_key].append(key)
        else:
            dict[tmp_key]=[]
            dict[tmp_key].append(key)

    print(dict)


if __name__ == "__main__":
    lst=["eat", "tea", "tan", "ate", "nat", "bat"]
    GroupingAnagrams(lst)