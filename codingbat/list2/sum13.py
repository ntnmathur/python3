# Return the sum of the numbers in the array, returning 0 for an empty array.
# Except the number 13 is very unlucky, so it does not count and numbers
# that come immediately after a 13 also do not count.
#
#
# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6

def sum13(lst):
    flag = False
    sum = 0
    for i in range(len(lst)):
        if lst[i] == 13:
            flag = True
        elif flag == True:
            flag = False
        else:
            sum = sum + lst[i]
    return sum

if __name__ == "__main__":

    print(sum13([1, 2, 2, 1]))
    print(sum13([1, 1]))
    print(sum13([1, 2, 2, 1, 13]))