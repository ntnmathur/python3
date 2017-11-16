def structure_string(s):
    fnl_list = split(s)
    return ' '.join(fnl_list)

def split(s):
    word = []
    words = []
    for c in s:
        if c != ' ':
            word.append(c)
        else:
            if word:
                words.append(''.join(word))
                word = []
    if word:
        words.append(''.join(word))
    return words


if __name__ == "__main__":
    str1 = '    The     sky is     very blue     '
    s = structure_string(str1)
    print(s)