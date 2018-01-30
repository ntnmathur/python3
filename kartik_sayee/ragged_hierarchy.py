def get_it(relation):
    parents = [x[0] for x in relation]
    # children = [x[1] for x in relation]
    # root = (set(parents) - set(children)).pop()
    # print(root)
    hash_map = {}
    for parent in parents:
        hash_map[parent] = get_all_kids(relation,parent)
    # print(hash_map)
    return generate_from_map(hash_map)

def get_all_kids(relation, parent):
    stock = get_children(relation,parent)
    all_kids = []
    all_kids.extend(stock)
    while stock:
        new_kids = get_children(relation, stock.pop())
        stock.extend(new_kids)
        all_kids.extend(new_kids)
    return all_kids


def get_children(relation, node):
    children = []
    for tup in relation:
        if tup[0] == node:
            children.append(tup[1])
    return children

def generate_from_map(hash_map):
    ragged_hierarchy = []
    for key in hash_map:
        ragged_hierarchy.append((key,key))
        for elem in hash_map[key]:
            ragged_hierarchy.append((key,elem))
            ragged_hierarchy.append((elem,elem))
    return set(ragged_hierarchy)

relation = [('all','web'),('all','mobile'),('web','windows'),('web','mac'),('mobile','ios'),('mobile','android'),('ios','iphone'),('ios','ipad')]
print(get_it(relation))