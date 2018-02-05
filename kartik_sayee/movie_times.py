# def MovieTimes(tup_list):
#     print("tup_list:", tup_list)
#     sorted_list = sorted(tup_list, key = lambda x:x[0])
#     print("tup_list sorted:", sorted_list)
#     fnl_lst = []
#     fnl_lst.append(tup_list[0])
#     k=0
#     i=1
#     # 1 5 7 10
#     # (1,3) (2,5) (3,4) (7,10)
#     # -> (1,5) (3,4) (7,10)
#     # --> (1,5) (7,10)
#     while i < len(sorted_list):
#         if sorted_list[i][0] < fnl_lst[k][1]:
#             if sorted_list[i][1] < fnl_lst[k][1]:
#                 tmp = (fnl_lst[k][0], fnl_lst[k][1])
#             else:
#                 tmp = (fnl_lst[k][0], sorted_list[i][1])
#             del fnl_lst[k]
#             fnl_lst.append(tmp)
#         else:
#             fnl_lst.append(sorted_list[i])
#             k += 1
#         i += 1
#     print("final list merged:", fnl_lst)
#
#     sum = 0
#     for sublist in fnl_lst:
#         sum = sum + (sublist[1] - sublist[0])
#
#     return sum

def MovieTimes(intervals):
    sorted_by_lower_bound = sorted(intervals, key=lambda tup: tup[0])
    merged = []
    print(sorted_by_lower_bound)
    for higher in sorted_by_lower_bound:
        if not merged:
            merged.append(higher)
        else:
            lower = merged[-1]
            # test for intersection between lower and higher:
            # we know via sorting that lower[0] <= higher[0]
            if higher[0] <= lower[1]:
                upper_bound = max(lower[1], higher[1])
                merged[-1] = (lower[0], upper_bound)  # replace by merged interval
            else:
                merged.append(higher)
        print(merged)
        print('----------------------')
    return merged

def get_sum(merged):
    sum = 0
    for tup in merged:
        minutes = tup[1] - tup[0]
        sum += minutes
    return sum


if __name__ == "__main__":
    tup_list=[(0,15),(20,29),(40,50),(10,30),(45,54),(55,65)]
    merged = MovieTimes(tup_list)
    print(MovieTimes(tup_list))

    print(get_sum(merged))