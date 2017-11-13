def ReplaceSpaces(str1):
    words = [x for x in str1.split('$') if x != '']
    return '%20'.join(words)


if __name__ == "__main__":
    str1 = '$$$$$Mr$$John$Smith$$$$$$'
    str2 = 'Mr$$John$Smith'
    str3 = '$$$$$Mr$$John$Smith'
    str4 = '$$$$$Mr$$John$$$$Smith$'
    print(ReplaceSpaces(str1))
    print(ReplaceSpaces(str2))
    print(ReplaceSpaces(str3))
    print(ReplaceSpaces(str4))