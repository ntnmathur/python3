# Question:
# Given an input string s, reverse the string word by word.
# For example, given s = "the sky is blue", return "blue is sky the".


class ReverseString(object):
    def __init__(self, string: str) -> None:
        self.string = string

    def reverse(self) -> str:
        # word_list = self.string.split(" ")
        word_list = self.split()
        print("word_list:", word_list)
        i = len(word_list) - 1
        print("i:", i)
        reverse_list = []
        while i >= 0:
            reverse_list.append(word_list[i])
            print("reverse_list:", reverse_list)
            i -= 1
        return " ".join(reverse_list)

    def split(self) -> list:
        word = []
        words = []
        for char in self.string:
            if char not in " ":
                word.append(char)
            else:
                if word:
                    words.append(''.join(word))
                    word = []
        if word:
            words.append(''.join(word))
        return words

if __name__ == "__main__":
    obj = ReverseString("My name is Nitin").reverse()
    print(obj)

