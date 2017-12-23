def string_word_freq(s):
    word_list = s.split()
    hash_map = {}
    for word in word_list:
        if word in hash_map:
            hash_map[word] = hash_map[word] + 1
        else:
            hash_map[word] = 1
    return hash_map.items()


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
print(string_word_freq(s))