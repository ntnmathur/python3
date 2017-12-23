def vowel_count(str1):
    vowels = 'aeiou'
    return len([x for x in str1 if x in vowels])

print(vowel_count('w3resource'))