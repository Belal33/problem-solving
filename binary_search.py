import unittest


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            high = mid - 1
        if arr[mid] < target:
            low = mid + 1
        if arr[mid] == target:
            return mid
    return -1


class BinarySearchTest(unittest.TestCase):
    def test_search_1(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 5
        self.assertEqual(binary_search(arr, target), 4)

    def test_search_2(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 1
        self.assertEqual(binary_search(arr, target), 0)

    def test_search_3(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 9
        self.assertEqual(binary_search(arr, target), 8)

    def test_search_4(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 10
        self.assertEqual(binary_search(arr, target), -1)

    def test_search_5(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 0
        self.assertEqual(binary_search(arr, target), -1)

    def test_search_6(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 6
        self.assertEqual(binary_search(arr, target), 5)

    def test_search_7(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 3
        self.assertEqual(binary_search(arr, target), 2)

    def test_search_8(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 8
        self.assertEqual(binary_search(arr, target), 7)

    def test_search_9(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        target = 2
        self.assertEqual(binary_search(arr, target), 1)


if __name__ == "__main__":
    unittest.main()
