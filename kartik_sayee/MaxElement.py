def MaxElement(ary):
    max_elem = ary[0]
    for elem in ary:
        if elem > max_elem:
            max_elem = elem
    return max_elem

if __name__ == "__main__":
    ary = [5, 89, 20, 64, 20, 45, 53]
    print(MaxElement(ary))