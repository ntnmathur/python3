def swap_dot_comma(str1):
    comma_idx = str1.index(',')
    dot_idx = str1.index('.')
    if comma_idx > dot_idx:
        return str1[:dot_idx] + ',' + str1[dot_idx+1:comma_idx] + '.' + str1[comma_idx+1:]
    else:
        return str1[:comma_idx] + ',' + str1[comma_idx+1:dot_idx] + '.' + str1[dot_idx+1:]


amount = "32.054,23"
print(swap_dot_comma(amount))
