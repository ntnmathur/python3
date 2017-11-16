def UniqueDigits(n):
    num = n
    hash_map = {}
    while num > 0:
        digit = num % 10
        # print("digit:" + str(digit))
        if digit in hash_map:
            return False
        hash_map[digit] = 1
        num = int(num/10)
        # print("num:", num)
    return True

if __name__ == "__main__":
    n=4592
    print(UniqueDigits(n))

    n=1998
    print(UniqueDigits(n))
