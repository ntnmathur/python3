def NumberPalindrome(num):

    n = num
    reverse = 0

    while n > 0:
        remainder = n % 10
        reverse = reverse*10 + remainder
        n = int(n/10)

    if num == reverse:
        return True
    else:
        return False

if __name__ == "__main__":
    num = 112211
    print(NumberPalindrome(num))

    num = 3344882
    print(NumberPalindrome(num))