def get_friends(lst):
    hash_map = {}
    for l in lst:
        print ("l", l)
        if len(l) == 2:
            for elem in l:
                print ("elem", elem)
                check_add_dict(elem, hash_map, False)
                print("dict", hash_map)
        else:
            check_add_dict(l[0], hash_map, True)
            print("dict", hash_map)
        print("*******************************")
    return hash_map


def check_add_dict(elem, hash_map,single):
    if elem in hash_map:
        hash_map[elem] = hash_map[elem] + 1
    else:
        if single:
            hash_map[elem] = 0
        else:
            hash_map[elem] = 1


if __name__ == "__main__":
    lst = [['A','B'], ['B','C'], ['A','D'], ['A','C'], ['E']]
    friend_dict = get_friends(lst)
    print(friend_dict)
    # {'A': 3, 'B': 2, 'C': 2, 'D': 1, 'E': 0}