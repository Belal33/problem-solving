import unittest
import random


def bubble_sort(arr: list[int]):
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


arr = [5, 1, 4, 2, 3, 2, 5, 4, 54, 5443, 435, 34345, 34, 534, 5, 345, 435, 345, 3]


# test cases
class BubbleSortTest(unittest.TestCase):
    def test_sort_1(self):
        arr = random.sample(range(10, 30), random.randint(3, 10))
        print(bubble_sort((arr)), sorted(arr))
        self.assertEqual(bubble_sort((arr)), sorted(arr))

    def test_sort_2(self):
        arr = random.sample(range(10, 30), random.randint(3, 10))
        print(bubble_sort((arr)), sorted(arr))
        self.assertEqual(bubble_sort((arr)), sorted(arr))

    def test_sort_3(self):
        arr = random.sample(range(10, 30), random.randint(3, 10))
        print(bubble_sort((arr)), sorted(arr))
        self.assertEqual(bubble_sort((arr)), sorted(arr))

    def test_sort_4(self):
        arr = random.sample(range(10, 30), random.randint(3, 10))
        print(bubble_sort((arr)), sorted(arr))
        self.assertEqual(bubble_sort((arr)), sorted(arr))

    def test_sort_5(self):
        arr = random.sample(range(10, 30), random.randint(3, 10))
        print(bubble_sort((arr)), sorted(arr))
        self.assertEqual(bubble_sort((arr)), sorted(arr))

    def test_sort_6(self):
        arr = random.sample(range(10, 30), random.randint(3, 10))
        print(bubble_sort((arr)), sorted(arr))
        self.assertEqual(bubble_sort((arr)), sorted(arr))

    def test_sort_7(self):
        arr = [4, 2, 2, 8, 5, 3]
        print(bubble_sort((arr)), sorted(arr))
        self.assertEqual(bubble_sort((arr)), sorted(arr))


if __name__ == "__main__":
    unittest.main()
