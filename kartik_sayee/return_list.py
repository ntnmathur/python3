def ReturnList(n):
    lst = []
    while n != 0:
        print(n)
        digit = n % 10
        lst.append(digit)
        n = int(n/10)
    return reverse(lst)


def reverse(lst):
    i = len(lst) - 1
    rev = []
    while i >= 0:
        rev.append(lst[i])
        i -= 1
    print(rev)
    return rev


if __name__ == "__main__":
    n=123
    ReturnList(n)

    n = 4000
    ReturnList(n)