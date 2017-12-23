def permute(num):
    if len(num) == 1:
        return [num]

    prev_permutations = permute(num[1:])
    first_num = num[0]
    result = []
    for elem in prev_permutations:
        for i in range(len(prev_permutations) + 1):
            if (elem[:i] + [first_num] + elem[i:]) not in result:
                result.append(elem[:i] + [first_num] + elem[i:])
    return result

my_nums = [1,2,3,4,7,8]
print("Original Cofllection: ",my_nums)
all = permute(my_nums)
print(len(all))
print("Collection of distinct numbers:\n",permute(my_nums))
