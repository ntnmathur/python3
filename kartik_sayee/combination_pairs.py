def pair_combinations(lst):
    collector = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] != lst[j]:
                collector.append((lst[i],lst[j]))
            else:
                collector.append(lst[i])
    collector.append(tuple(lst))
    return collector

print(pair_combinations(['uk','us','india']))