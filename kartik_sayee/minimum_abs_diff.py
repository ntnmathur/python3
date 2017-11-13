import sys


def MinAbsDiff(ary):
    min_diff = sys.maxsize
    for i in range(len(ary)):
        for j in range(i+1, len(ary)):
            diff = abs(ary[i] - ary[j])
            if diff < min_diff:
                min_diff = diff
    return min_diff


if __name__ == "__main__":
    ary = [30, 5, 20, 9]
    print(MinAbsDiff(ary))