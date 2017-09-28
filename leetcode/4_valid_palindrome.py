# Question:
# Given a string, determine if it is a palindrome, considering only alphanumeric characters
# and ignoring cases.
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
# Example Questions Candidate Might Ask:
# Q: What about an empty string? Is it a valid palindrome?
# A: For the purpose of this problem, we define empty string as valid palindrome.
#


class Palindrome(object):
    def __init__(self, s: str)-> None:
        self.s = s

    def is_palindrome(self) -> bool:
        lower_s = self.s.lower()
        i = 0
        j = len(lower_s) - 1
        while i < j:
            if lower_s[i] != lower_s[j]:
                return False
            i += 1
            j -= 1
        return True

if __name__ == "__main__":

    s1 = "Nitin"
    obj1 = Palindrome(s1).is_palindrome()
    print(obj1)
    assert obj1 == True

    s2 = "HeMan"
    obj2 = Palindrome(s2).is_palindrome()
    print(obj2)
    assert obj2 == False
