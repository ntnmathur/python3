def reverse_words(str1):
    str_list = str1.split()
    reverse = []
    for w in str_list:
        reverse.append(reverse_word(w))
    return ' '.join(reverse)


def reverse_word(word):
    reverse = []
    i = len(word)-1
    while i >= 0:
        if i == len(word)-1:
            reverse.append(word[i].upper())
        else:
            reverse.append(word[i].lower())
        i -= 1
    return ''.join(reverse)

if __name__ == "__main__":
    str1 = 'The Sky is Blue'
    s = reverse_words(str1)
    print(s)