def unique_char_string(string):
    hash_map = {}
    for c in string:
        if c in hash_map:
            return False
        else:
            hash_map[c] = 1
    return True


if __name__ == "__main__":
    s = unique_char_string("Nitin")
    print(s)

    s1 = unique_char_string("abcde")
    print(s1)