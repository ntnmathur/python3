def unique_digits(n):
    s = set()
    for c in str(n):
        s.add(c)
    return s


if __name__ == "__main__":
    s = unique_digits(475848354)
    print(s)
