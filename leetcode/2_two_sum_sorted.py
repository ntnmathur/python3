# Similar to Question [1. Two Sum], except that the input array is already sorted in
# ascending order.


class TwoSumSorted(object):
    def __init__(self, array: list, target: int) -> None:
        self.array = array
        self.target = target

    def two_sum_sorted(self) -> (int, int):
        for index, num in enumerate(self.array):
            next_index = self.binary_search(self.target - num, index)
            if next_index != -1:
                return index, next_index
            else:
                pass

        raise Exception("Unable to find two sum")

    def binary_search(self, key: int, start: int) -> int:
        array = self.array
        print("array:", array)
        print("Trying to find index of:", key)
        left = start
        right = len(array) - 1
        while left < right:
            print("left:", left)
            print("right", right)
            middle = int((left+right)/2)
            print("middle", middle)
            if array[middle] < key:
                left = middle + 1
            else:
                right = middle

        if left == right and array[left] == key:
            print("key found:", left)
            return left
        else:
            print("key not found")
            return -1

if __name__ == "__main__":
    array = [1, 5, 3, 4, 7, 7, 2, 3]
    obj1 = TwoSumSorted(sorted(array), 9)
    actual = obj1.two_sum_sorted()
    expected = (1, 6)
    assert actual == expected
    print("actual:",actual)
    # obj1.binary_search(2,0)

