def return_balanced(input_str):
    if len(input_str) == 0:
        return None
    pushChars, popChars = "<({[", ">)}]"
    stack = []
    input_str = [c for c in input_str if c in pushChars or c in popChars]
    # print(input_str)
    for char in input_str:
        if char in pushChars:
            stack.append(char)
        elif char in popChars:
            if len(stack) == 0:
                return False
            else:
                popped = stack.pop()
                balancing_bracket = pushChars[popChars.index(char)]
                if popped != balancing_bracket:
                    return False
        # else:
        #     return False
    return not len(stack)


assert return_balanced('') == None
assert return_balanced('This<might>not(be{balanced}') == False
assert return_balanced('{(<[SimpleExampleForBalanced]>)}') == True
assert return_balanced('{)(<[This]is>not)balanced}') == False
assert return_balanced('{(<[simple])>}') == False
assert return_balanced('{Another{Example<of>Unbalanced}String') == False
assert return_balanced('(This)is<how>balanced{string}with[paranthesis]canbe') == True
print('passed')