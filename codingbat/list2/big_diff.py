
# Given an array length 1 or more of ints, return the difference
# between the largest and smallest values in the array.
# Note: the built-in min(v1, v2) and max(v1, v2)
# functions return the smaller or larger of two values.
#
#
# big_diff([10, 3, 5, 6]) → 7
# big_diff([7, 2, 10, 9]) → 8
# big_diff([2, 10, 7, 2]) → 8

def big_diff(lst):
    largest = lst[0]
    smallest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return largest - smallest

if __name__ == "__main__":

    print(big_diff([10, 3, 5, 6]))
    print(big_diff([7, 2, 10, 9]))
    print(big_diff([2, 10, 7, 2]))