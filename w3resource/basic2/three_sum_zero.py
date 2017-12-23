# 4. Write a Python program to find unique triplets whose three elements gives the sum of zero from an array
# of n integers. Go to the editor

def three_sum(lst):
    answer_set=[]
    for i in range(len(lst)-2):
        hash_map = {}
        for j in range(i+1, len(lst)-1):
            if -(lst[i]+lst[j]) in hash_map:
                answer_set.append((lst[i], lst[j], -(lst[i]+lst[j])))
            else:
                hash_map[j] = 0
    return answer_set

x = [1, -6, 4, 2, -1, 2, 0, -2, 0 ]
print(three_sum(x))


