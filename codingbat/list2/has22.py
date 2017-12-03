
# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

# has22([1, 2, 2]) → True
# has22([1, 2, 1, 2]) → False
# has22([2, 1, 2]) → False

def has22(lst):
    for i in range(len(lst)-1):
        if lst[i] == 2 and lst[i+1] == 2:
            return True
    return False

if __name__ == "__main__":

    print(has22([1, 2, 2]))
    print(has22([1, 2, 1, 2]))
    print(has22([2, 1, 2]))