import collections

def RemoveDuplicates(ary):

    final_dict = collections.OrderedDict()
    for elem in ary:
        final_dict[elem] = 0
    return final_dict.keys()

if __name__ == "__main__":
    ary = [1, 1, 1, 2, 2, 3, 5, 5, 7, 7, 7, 8, 9, 10, 34, 34, 56, 56, 56]
    print(RemoveDuplicates(ary))