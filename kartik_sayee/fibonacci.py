def fib(n):
    fil_lst = []
    fil_lst.append(0)
    fil_lst.append(1)
    for i in range(2, n-1):
        fil_lst.append(fil_lst[i-1]+fil_lst[i-2])
    return fil_lst


if __name__ == "__main__":

    print(fib(10))







