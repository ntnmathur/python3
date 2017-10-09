
def sum13(nums):
    sum = 0
    take_out = 0
    for i in range(len(nums)):
        if nums[i] != 13:
            sum += nums[i]
        else:
            if i != len(nums)-1 or 1!=0:
                take_out =+ nums[i+1]
        print("i:", i)
        print("nums[i]:", nums[i])
        print("sum:", sum)
        print("**********BREAK**********")
    print("sum:", sum)
    print("take_out:", take_out)
    return sum-take_out


if __name__ == "__main__":
    s = sum13([1, 2, 2, 1])
    print(s)
