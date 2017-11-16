# def ReplaceStr(str):
#
#     print(str)
#     fnl_str=str.replace('fun','NONE')
#     print(fnl_str)
#     print(fnl_str.count('NONE'))


def ReplaceStr(str):

    print(str)
    # fnl_str=replace_x(str, 'fun','NONE')
    replacer = 'NONE'
    to_replace = 'fun'
    fnl_str = replacer.join(str.split(to_replace))
    print("fnl_str:"+ fnl_str)
    # print(fnl_str.count('NONE'))


def replace_x(str, to_replace, replacer):
    for i in range(len(str)):
        # print(to_replace, str[i:i+len(to_replace)])
        if to_replace == str[i:i+len(to_replace)]:
            base_string = []
            base_string.append(str[:i])
            base_string.append(replacer)
            base_string.append(str[i+len(to_replace):])
            str = ''.join(base_string)
    return ''.join(base_string)

if __name__ == "__main__":
    str1 = "Amazon is a fun place to fun work and is very fun to be"
    ReplaceStr(str1)