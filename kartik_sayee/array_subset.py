def is_array_subset(arr1, arr2):
    if len(arr1) > len(arr2):
        small = arr2
        big = arr1
    else:
        small = arr1
        big = arr2

    hash_map = {}
    for elem in big:
        if elem in hash_map:
            hash_map[elem] = hash_map[elem] + 1
        else:
            hash_map[elem] = 1

    for elem in small:
        if elem in hash_map and hash_map[elem] > 0:
            hash_map[elem] = hash_map[elem] - 1
        else:
            return False

    return True


if __name__ == "__main__":
    s = is_array_subset("nitin", "tin")
    print(s)
    s = is_array_subset("nitin", "bob")
    print(s)