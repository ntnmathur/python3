# 45. Write a Python program to check if a string contains all letters of the alphabet

def check_all_alpha(str1):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    return set(str1.lower()) >= set(alphabets)

# input_string = 'The quick brown fox jumps over the lazy dog'
# print(check_all_alpha(input_string))
# input_string = 'The quick brow fox jumps over the lazy dog'
# print(check_all_alpha(input_string))

#  44. Write a Python program to print the index of the character in a string
def print_char_index(str1):
    for (position, character) in enumerate(str1):
        print('Current character ' + str(character) + ' position at ' + str(position))

# print_char_index('w3resource')

# 42. Write a python program to count repeated characters in a string.
def count_repeat(str1):
    hash_map={}
    for c in str1:
        if c in hash_map:
            hash_map[c] = hash_map[c] + 1
        else:
            hash_map[c] = 1
    # print(hash_map)
    return {k:v for (k,v) in hash_map.items() if v > 1}
#
# s = 'thequickbrownfoxjumpsoverthelazydog'
# print(count_repeat(s))

# 41. Write a Python program to strip a set of characters from a string.
def strip_char(str,chars):
    return ''.join(c for c in str if c not in chars)

# print(strip_char("The quick brown fox jumps over the lazy dog.", "aeiou"))

# 40. Write a Python program to reverse words in a string.
def reverse_words(text):
    for line in text.split('\n'):
        return ' '.join(line.split()[::-1])

# print(reverse_words("The quick brown fox jumps over the lazy dog."))
# print(reverse_words("Python Exercises."))

# 39. Write a Python program to reverse a string.
def reverse_string(str):
    rev = []
    idx = len(str) - 1
    while idx > 0:
        rev.append(str[idx])
        idx -=1
    return ''.join(rev)
# print(reverse_string("abcdef"))
# print(reverse_string("Python Exercises."))

# 38. Write a Python program to count occurrences of a substring in a string.
def find_occurences(str, substr):
    len_substr = len(substr)
    cnt = 0
    for i in range(len(str)-len_substr):
        if str[i:i+len_substr] == substr: # VERY IMPORTANT
            cnt +=1
    return cnt

# str1 = 'the quick brown fox jumps over the lazy dog.'
# print(find_occurences(str1,'the'))
# print(find_occurences(str1,'fox'))

# 25. Write a Python program to create a Caesar encryption.
def caesar_encrypt(real_text, step):
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    out = []
    for c in real_text:
        if c in uppercase:
            idx = uppercase.index(c)
            cryp_idx = (idx+step)%26
            out.append(uppercase[cryp_idx])
        elif c in lowercase:
            idx = lowercase.index(c)
            cryp_idx = (idx+step)%26
            out.append(lowercase[cryp_idx])
        else:
            out.append(c)

    return ''.join(out)
# code = caesar_encrypt('My name is Nitin.', 2)
# print(code)

# 24, Write a Python program to check whether a string starts with specified characters.
def starts_with(str, strt):
    # return str.startswith(str)
    l = len(strt)
    if str[:l] == strt:
        return True
    else:
        return False


# string = "w3resource.com"
# print(starts_with(string, "w3r"))

# 23. Write a Python program to remove a newline in Python.
def remove_newline(str):
    return ''.join(c for c in str if c != '\n')

# str1='Python Exercises\n'
# print(remove_newline(str1))

# 22.Write a Python program to sort a string lexicographically.
def lex_sort(str):
    return ''.join(sorted(str))

# print(lex_sort('w3resource'))
# print(lex_sort('quickbrown'))

# 21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
def to_uppercase(str1):
    num_uppercase = 0
    for char in str1[:4]:
        if char.upper() == char:
            num_uppercase += 1
    if num_uppercase >=2:
        return str1.upper()
    else:
        return str1

# print(to_uppercase('Python'))
# print(to_uppercase('PyThon'))

# 20. Write a Python function to reverses a string if it's length is a multiple of 4.
def reverse_string(str1):
    if len(str1)%4 == 0:
        return ''.join(reversed(str1))
    else:
        return str1
# print(reverse_string('abcd'))
# print(reverse_string('python'))

# # 19. Write a Python program to get the last part of a string before a specified character.
# str1 = 'https://www.w3resource.com/python-exercises/string'
# print(str1.rsplit('/',1)[1])
# print(str1.rsplit('-',1)[1])

# 16. Write a Python function to insert a string in the middle of a string.
def insert_sting_middle(str, word):
    l = len(str)
    return str[:int(l/2)] + word + str[int(l/2):]

# print(insert_sting_middle('[[]]', 'Python'))
# print(insert_sting_middle('{{}}', 'PHP'))
# print(insert_sting_middle('<<>>', 'HTML'))

# 15. Write a Python function to create the HTML string with tags around the word(s).
def add_tags(tag, text):
    return '<' + tag + '>' + text + '</'+tag+'>'

# print(add_tags('i', 'Python'))
# print(add_tags('b', 'Python Tutorial'))

# 14. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
def return_sorted_words(comma_sep_text):
    words = comma_sep_text.split(',')
    return ','.join(sorted(words))

print(return_sorted_words('red,black,pink,green'))