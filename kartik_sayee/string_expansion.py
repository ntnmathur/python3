def string_expansion(string):
    fnl_list = []
    i=0
    while i <= len(string)-1:
        char = string[i]
        times = int(string[i+1])
        fnl_list.append(times*char)
        i += 2
    return ''.join(fnl_list)


if __name__ == "__main__":
    str1 = 'a3b1c5a2'
    s = string_expansion(str1)
    print(s)