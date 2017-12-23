def permutations(word):
    if len(word)<=1:
        return [word]

    #get all permutations of length N-1
    perms=permutations(word[1:])
    char=word[0]
    result=[]

    print("word:", word)
    print("perms:", perms)
    print("char:", char)
    #iterate over all permutations of length N-1
    for perm in perms:
        # insert the character into every possible location - number of locations is chars+1 ex
        # ex: abc  (1)a(2)b(3)c(4) -> 4 locations
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
    print("result:", result)
    print("========================")
    return result

if __name__ == "__main__":
    print(permutations('abcde'))