
# 1) Print Max element of a given list
# 2) Print median of a given list
# 3) Print the first nonrecurring element in a list
# 4) Print the most recurring element in a list
# 5) Greatest common Factor


def first_non_rec(nums: list):
    order = []
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] = counts[num] + 1
        else:
            counts[num] = 1
            order.append(num)
    for o in order:
        if counts[o] ==1:
            return o
    return None


def most_rec(nums: list):
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] = counts[num] + 1
        else:
            counts[num] = 1

    max_key = counts[nums[0]]
    for k,v in counts.items():
        if v > counts[max_key]:
            max_key = k
    return max_key


def maximum(nums: list) -> int:
    max_elem = nums[0]
    for num in nums:
        max_elem = max(max_elem, num)
    return max_elem


def median(nums: list):
    nums.sort()
    length = len(nums)
    if length < 1:
        return None
    elif length % 2 !=0:
        index = int(length/2)
        return nums[index]
    else:
        index1 = int((length-1)/2)
        index2 = int((length-1)/2) + 1
        return int((nums[index1]+nums[index2])/2)


def gcd(m, n):
    big = max(m,n)
    small = min(m,n)

    while big % small !=0:
        rem = big % small
        big = small
        small = rem
    return small


def lcm(m,n):
    return (m*n)/gcd(m,n)


def lcm2(m,n):
    greater = max(m,n)
    while (True):
        if greater % m == 0 and greater % n == 0:
            lcm = greater
        greater +=1
    return lcm

if __name__ == "__main__":
    max_elem = maximum([1,2,3,4,5,6,7])
    print("max:",max_elem)

    m = median([1,5,88,2,3,4,5,6,7])
    print("median:", m)

    f = first_non_rec([1,1,2,2,2,3])
    print("f:", f)

    most_rec = most_rec([7,7,7,7,3,3,3,4,4,4,4,4,6,6,6,6,6,6,6,6,6,6])
    print("most_rec:", most_rec)