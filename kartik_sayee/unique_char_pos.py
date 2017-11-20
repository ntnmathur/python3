def UniqueCharPos(str):
    for i in range(len(str)):
        if str[i] not in str[i+1:]:
            print(str[i], i)
            break


if __name__ == "__main__":
    str='leetcode'
    UniqueCharPos(str)

    str = 'loveleetcode'
    UniqueCharPos(str)