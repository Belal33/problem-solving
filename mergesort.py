import unittest
import random


def merge_sort(arr: list[int], start: int, end: int):
    m_s(arr, start, end)
    return arr


def m_s(arr: list[int], start: int, end: int):
    if end - 1 <= start:
        return
    mid = (start + end - 1) // 2
    m_s(arr, start, mid + 1)
    m_s(arr, mid + 1, end)
    merge(arr, start, mid, end)


def merge(arr: list[int], start: int, mid: int, end: int) -> None:
    i = j = 0
    k = start

    left_arr = arr[start : mid + 1]
    right_arr = arr[mid + 1 : end]
    # print(left_arr, right_arr)

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
            k += 1
        else:
            arr[k] = right_arr[j]
            j += 1
            k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


class IsertionTest(unittest.TestCase):
    def test_sort_1(self):
        arr = random.sample(range(10, 30), random.randint(3, 10))
        print(merge_sort(arr, 0, len(arr)), sorted(arr))
        self.assertEqual(merge_sort(arr, 0, len(arr)), sorted(arr))

    def test_sort_2(self):
        arr = random.sample(range(10, 30), random.randint(3, 10))
        print(merge_sort(arr, 0, len(arr)), sorted(arr))
        self.assertEqual(merge_sort(arr, 0, len(arr)), sorted(arr))

    def test_sort_3(self):
        arr = random.sample(range(10, 30), random.randint(3, 10))
        print(merge_sort(arr, 0, len(arr)), sorted(arr))
        self.assertEqual(merge_sort(arr, 0, len(arr)), sorted(arr))

    def test_sort_4(self):
        arr = random.sample(range(10, 30), random.randint(3, 10))
        print(merge_sort(arr, 0, len(arr)), sorted(arr))
        self.assertEqual(merge_sort(arr, 0, len(arr)), sorted(arr))

    def test_sort_5(self):
        arr = random.sample(range(10, 30), random.randint(3, 10))
        print(merge_sort(arr, 0, len(arr)), sorted(arr))
        self.assertEqual(merge_sort(arr, 0, len(arr)), sorted(arr))

    def test_sort_6(self):
        arr = random.sample(range(10, 30), random.randint(3, 10))
        print(merge_sort(arr, 0, len(arr)), sorted(arr))
        self.assertEqual(merge_sort(arr, 0, len(arr)), sorted(arr))


if __name__ == "__main__":
    unittest.main()
