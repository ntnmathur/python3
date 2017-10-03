# Question:
# Implement strstr(). Returns the index of the first occurrence of needle in haystack, or –1
# if needle is not part of haystack.
# O(nm) runtime, O(1) space – Brute force:
# There are known efficient algorithms such as Rabin-Karp algorithm, KMP algorithm, or
# the Boyer-Moore algorithm. Since these algorithms are usually studied in an advanced
# algorithms class, it is sufficient to solve it using the most direct method in an interview –
# The brute force method.
# The brute force method is straightforward to implement. We scan the needle with the
#     haystack from its first position and start matching all subsequent letters one by one. If one
# of the letters does not match, we start over again with the next position in the haystack.
# Assume that n = length of haystack and m = length of needle, then the runtime
# complexity is O(nm).
# Have you considered these scenarios?
# i. needle or haystack is empty. If needle is empty, always return 0. If haystack is
# empty, then there will always be no match (return –1) unless needle is also
# empty which 0 is returned.
#     ii. needle’s length is greater than haystack’s length. Should always return –1.
# iii. needle is located at the end of haystack. For example, “aaaba” and “ba”. Catch
# possible off-by-one errors.
# iv. needle occur multiple times in haystack. For example, “mississippi” and
# “issi”. It should return index 2 as the first match of “issi”.
# v. Imagine two very long strings of equal lengths = n, haystack = “aaa…aa” and
# needle = “aaa…ab”. You should not do more than n character comparisons, or
# else your code will get Time Limit Exceeded in OJ.


class StrInStr(object):
    def __init__(self, needle: str, haystack: str) -> None:
        self.needle = needle
        self.haystack = haystack

    def is_present(self) -> int:
        for i in range(len(self.haystack)):
            for j in range(len(self.needle)):
                print("i:", i)
                print("j:", j)
                print("self.needle[j]",self.needle[j])
                print("self.haystack[i+j]",self.haystack[i+j])
                if self.needle[j] != self.haystack[i+j]:
                    print("************BREAK**************")
                    break
                elif j == len(self.needle)-1:
                    return i
        return -1


if __name__ == "__main__":
    index1 = StrInStr("tin", "nitin").is_present()
    print("index1:",index1)
    assert index1 == 2
    index2 = StrInStr("nit", "nitin").is_present()
    print("index2:",index2)
    assert index2 == 0
    index3 = StrInStr("in", "nitin").is_present()
    print("index3:",index3)
    assert index3 == 3