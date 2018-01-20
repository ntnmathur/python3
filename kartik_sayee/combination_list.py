import copy
def combinations(target,data,collector=[]):
    for i in range(len(data)):
        new_target = copy.copy(target)
        new_target.append(data[i])
        new_data = data[i+1:]
        collector.append((new_target))
        print("new_target",new_target)
        print("new_data",new_data)
        print("collector",collector)
        print("------------------------")
        combinations(new_target,new_data,collector)
    return collector

print(combinations([],['us','uk','india']))