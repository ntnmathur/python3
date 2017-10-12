import collections

def string_compression(string):
    d = collections.OrderedDict()
    for c in string:
        if c in d:
            d[c] = d[c] + 1
        else:
            d[c] = 1
    fnl = []
    for k,v in d.items():
        fnl.append(str(k))
        fnl.append(str(v))
    return ''.join(fnl)


def string_compression2(string):
    prev = string[0]
    fnl_list = []
    cnt = 1
    for i in range(1,len(string)):
        if prev != string[i]:
            fnl_list.extend([prev,str(cnt)])
            cnt = 1
        else:
            cnt +=1
        prev = string[i]
    fnl_list.extend([prev,str(cnt)])
    return ''.join(fnl_list)


if __name__ == "__main__":
    str1 = 'aabcccccaa'
    s = string_compression(str1)
    print(s)

    str1 = 'aabcccccaa'
    s = string_compression2(str1)
    print(s)