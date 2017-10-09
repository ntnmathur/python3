def word_count(string):
    # word_list = string.split(' ')
    word_list = split(string)
    word_count_dict = {}
    for word in word_list:
        if word in word_count_dict:
            word_count_dict[word] = word_count_dict[word] + 1
        else:
            word_count_dict[word] = 1
    return word_count_dict


def split(string):
    words = []
    word = []
    for c in string:
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
    wc = word_count("Hello Hello dirty fellow - lo lo")
    print(wc)