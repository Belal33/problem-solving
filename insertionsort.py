import unittest
import random


def insertion_sort(arr: list[int]) -> list[int]:
    for i, el in enumerate(arr[1:], 1):
        # for j in range(i - 1, -1, -1):
        j = i - 1
        while j >= 0:
            if arr[j] > el:
                arr[j + 1] = arr[j]
            else:
                break
            j -= 1
        arr[j + 1] = el
    # ]
    return arr


class IsertionTest(unittest.TestCase):
    def test_sort_1(self):
        arr = random.sample(range(10, 30), random.randint(3, 10))
        print(insertion_sort(arr))
        self.assertEqual(insertion_sort(arr), sorted(arr))

    def test_sort_2(self):
        arr = random.sample(range(10, 30), random.randint(3, 10))
        print(insertion_sort(arr))
        self.assertEqual(insertion_sort(arr), sorted(arr))

    def test_sort_3(self):
        arr = random.sample(range(10, 30), random.randint(3, 10))
        print(insertion_sort(arr))
        self.assertEqual(insertion_sort(arr), sorted(arr))

    def test_sort_4(self):
        arr = random.sample(range(10, 30), random.randint(3, 10))
        print(insertion_sort(arr))
        self.assertEqual(insertion_sort(arr), sorted(arr))

    def test_sort_5(self):
        arr = random.sample(range(10, 30), random.randint(3, 10))
        print(insertion_sort(arr))
        self.assertEqual(insertion_sort(arr), sorted(arr))

    def test_sort_6(self):
        arr = random.sample(range(10, 30), random.randint(3, 10))
        print(insertion_sort(arr))
        self.assertEqual(insertion_sort(arr), sorted(arr))

    def test_sort_7(self):
        arr = list(range(10, 30))
        print(insertion_sort(arr))
        self.assertEqual(insertion_sort(arr), sorted(arr))


if __name__ == "__main__":
    # print(insertion_sort([1, 2, 3, 4, 9, 5, 6, 8, 10]))
    unittest.main()
