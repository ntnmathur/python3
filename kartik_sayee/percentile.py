def Percentile(ary, n):
    l = len(ary)-1
    ary.sort()
    for i in range(l):
        if i/l < n:
            continue
        else:
            break
    print(ary[i])

if __name__ == "__main__":
    ary = [5, 89, 20, 64, 20, 45]
    n = 0.75
    Percentile(ary, n)

    ary = [5, 89, 20, 64, 20, 45, 45, 23, 67, 32, 30]
    n = 0.9
    Percentile(ary, n)