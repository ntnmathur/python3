# Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other.

def check_all_nums_diff(lst):
    s = set()
    for num in lst:
        if num in s:
            return False
        else:
            s.add(num)
    return True

if __name__ == "__main__":
    print(check_all_nums_diff([1,2,3,4]))
    print(check_all_nums_diff([1,2,3,3]))