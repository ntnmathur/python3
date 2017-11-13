def AddingNumber(number):
    if number == 0:
        return number
    else:
        return number % 10 + AddingNumber(int(number/10))


if __name__ == "__main__":
    num = 38
    print(AddingNumber(num))

    num = 679
    print(AddingNumber(num))