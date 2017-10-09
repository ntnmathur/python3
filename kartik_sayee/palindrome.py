def is_palindrome(string):
    s = string.lower()
    i = 0
    j = len(s) - 1
    while (i<j):
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == "__main__":
    s = is_palindrome("Nitin")
    print(s)

    s = is_palindrome("Asia")
    print(s)