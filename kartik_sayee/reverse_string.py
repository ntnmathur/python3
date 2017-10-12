def ReverseString(str1):
    str_lst = str1.split()
    reverse = []
    i = len(str_lst)-1
    while i >=0 :
        reverse.append(str_lst[i])
        i -= 1
    return ' '.join(reverse)

if __name__ == "__main__":
    str1 = 'I am using hackerrank to improve programming'
    s = ReverseString(str1)
    print(s)