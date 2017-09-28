# Let’s assume we have two indices pointing to the ith and jth elements, Ai and Aj
# respectively. The sum of Ai and Aj could only fall into one of these three possibilities:
# i. Ai + Aj > target. Increasing i isn’t going to help us, as it makes the sum even
# bigger. Therefore we should decrement j.
# ii. Ai + Aj < target. Decreasing j isn’t going to help us, as it makes the sum even
# smaller. Therefore we should increment i.
# iii. Ai + Aj == target. We have found the answer.


class TwoSumSorted(object):
    def __init__(self, array: list, target: int) -> None:
        self.array = array
        self.target = target

    def two_sum_sorted(self) -> (int, int):
        i = 0
        j = len(self.array) - 1
        print("i:", i)
        print("j:", j)
        print("array", self.array)
        while i < j:
            sum = self.array[i] + self.array[j]
            print("sum", sum)
            print("aaray[i]", array[i])
            print("aaray[j]", array[j])
            print("sum", sum)
            if sum < self.target:
                i += 1
            elif sum > self.target:
                j -= 1
            else:
                return i, j

        raise Exception("Unable to find two sum")

if __name__ == "__main__":
    array = [1, 5, 3, 4, 7, 7, 2, 3]
    obj1 = TwoSumSorted(sorted(array), 9)
    actual = obj1.two_sum_sorted()
    expected = (1, 7)
    print("actual:", actual)
    assert actual == expected
    # obj1.binary_search(2,0)
