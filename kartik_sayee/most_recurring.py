def MostRecurringElement(ary):
    hash_map = {}
    for elem in ary:
        if elem in hash_map:
            hash_map[elem] = hash_map[elem] + 1
        else:
            hash_map[elem] = 1

    max_key = 0
    max_val = 0
    for k, v in hash_map.items():
        if v > max_val:
            max_key = k
            max_val = v
        else:
            pass

    return max_key, max_val


if __name__ == "__main__":
    ary = [4, 8, 4, 7, 8, 8, 5, 2, 7, 7, 7, 7, 3, 2, 1, 1]
    print(MostRecurringElement(ary))