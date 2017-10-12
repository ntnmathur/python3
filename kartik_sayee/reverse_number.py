def ReverseNumber(n):
    num = n
    reverse = 0
    i=len(str(num))-1
    while num >0:
        reminder = num %10
        reverse = reminder * (10**i) + reverse
        num = int(num/10)
        i -= 1
    return reverse


def ReverseNumber2(n):
    num = str(n)
    reverse = []
    i=len(str(num))-1
    while i >=0:
        reverse.append(num[i])
        i -= 1
    return ''.join(reverse)

if __name__ == "__main__":
    n = 34567
    num = ReverseNumber(n)
    print(num)

    n = 34567
    num = ReverseNumber2(n)
    print(num)