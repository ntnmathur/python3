# Question:
# Given an array of integers, find two numbers such that they add up to a specific target
# number.
# The function twoSum should return indices of the two numbers such that they add up to
# the target, where index1 must be less than index2. Please note that your returned answers
# (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution.


# O(n)
class TwoSum(object):

    def __init__(self, array: list, target: int)->None:
        self.int_array = array
        self.target = target

    def two_sum(self) -> tuple:
        hash_map = {}
        for index, num in enumerate(self.int_array):
            print("hash map" + str(hash_map))
            print("target:" + str(self.target))
            print("searching for (in map):" + str(self.target-num))
            if self.target - num in hash_map:
                return index, hash_map[self.target-num]
            else:
                hash_map[num] = index
        raise Exception("Unable to find two sum")

if __name__ == "__main__":
    obj1 = TwoSum([1, 5, 3, 4, 7, 7, 2, 3], 9)
    print("Main1")
    actual = obj1.two_sum()
    expected = (3, 1)
    assert actual == expected

    obj2 = TwoSum([1, 5, 3, 4, 7, 7, 2, 3], 5)
    print("Main2")
    actual = obj2.two_sum()
    expected = (3, 0)
    assert actual == expected
