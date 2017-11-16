import random


def fnl(i):
    return random.random()


def rand(st, end, n):
    return random.randrange(st, end, n)


def Random_sort(ary, n):
    print(random.randint(10, 200))
    print(sorted(ary, key=fnl)[:n])
    print(fnl(2))
    print(rand(100, 1000, 5))

if __name__ == "__main__":
    ary = [1,2,3,4,5,6,7,8,9]
    n = 5
    Random_sort(ary, 9)

    # Shuffle in place:
    random.shuffle(ary)
    print("Random Sort", ary)
