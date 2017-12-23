def string_char_freq(s):
    word_list = s.split()
    hash_map = {}
    for word in word_list:
        for char in word:
            if char in hash_map:
                hash_map[char.lower()] = hash_map[char.lower()] + 1
            else:
                hash_map[char.lower()] = 1
    return hash_map


s= """
United States Declaration of Independence
From Wikipedia, the free encyclopedia
The United States Declaration of Independence is the statement
adopted by the Second Continental Congress meeting at the Pennsylvania State
House (Independence Hall) in Philadelphia on July 4, 1776, which announced
that the thirteen American colonies, then at war with the Kingdom of Great
Britain, regarded themselves as thirteen independent sovereign states, no longer
under British rule. These states would found a new nation – the United States of
America. John Adams was a leader in pushing for independence, which was passed
on July 2 with no opposing vote cast. A committee of five had already drafted the
formal declaration, to be ready when Congress voted on independence.
"""
hash_map = string_char_freq(s)
sorted_map = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
print(sorted_map)