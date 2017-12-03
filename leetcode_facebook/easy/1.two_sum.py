# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution:
    @staticmethod
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for num in nums:
            if target-num in hash_map:
                return num, target-num
            else:
                hash_map[num] = 1

if __name__ == "__main__":

     print(Solution.twoSum([1, 5, 3, 4, 7, 7, 2, 3], 9))
     print(Solution.twoSum([1, 5, 3, 4, 7, 7, 2, 3], 5))
     print(Solution.twoSum([1, 5, 3, 4, 7, 7, 2, 3], 35))
