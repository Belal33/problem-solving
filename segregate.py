import unittest


def segregate_positive_negative(arr=[]):
    merge_segregate(arr, 0, len(arr) - 1)
    return arr


def merge_segregate(arr: list, start, end):
    mid = (start + end) // 2
    if start >= end:
        return

    # lerft half
    merge_segregate(arr, start, mid)

    # right half
    merge_segregate(arr, mid + 1, end)

    # merge
    left_arr = arr[start : mid + 1]
    right_arr = arr[mid + 1 : end + 1]
    left_i = 0
    right_i = 0
    arr_i = start

    while left_i < len(left_arr) and right_i < len(right_arr):
        # start segregating moving all negative to left
        if left_arr[left_i] < 0:
            arr[arr_i] = left_arr[left_i]
            left_i += 1
        elif right_arr[right_i] < 0:
            arr[arr_i] = right_arr[right_i]
            right_i += 1
        else:
            break
        arr_i += 1
    while left_i < len(left_arr):
        arr[arr_i] = left_arr[left_i]
        left_i += 1
        arr_i += 1
    while right_i < len(right_arr):
        arr[arr_i] = right_arr[right_i]
        right_i += 1
        arr_i += 1


# print(segregate_positive_negative([-1, 2, -3, 4, 5, 6, -7, 8, 9]))
# [-1, -3, -7, 4, 5, 6, 2, 8, 9]
# uint test
class TestSegregate(unittest.TestCase):
    def test_segregate_positive_negative_1(self):
        self.assertEqual(
            segregate_positive_negative([-1, 2, -3, 4, 5, 6, -7, 8, 9]),
            [-1, -3, -7, 2, 4, 5, 6, 8, 9],
        )

    def test_segregate_positive_negative_2(self):
        self.assertEqual(
            segregate_positive_negative([-1, 2, -3]),
            [-1, -3, 2],
        )

    def test_segregate_positive_negative_3(self):
        self.assertEqual(
            segregate_positive_negative([-1, 2, -3, 4, 5, 6, -7, 8, 9, -10]),
            [-1, -3, -7, -10, 2, 4, 5, 6, 8, 9],
        )

    def test_segregate_positive_negative_4(self):
        self.assertEqual(
            segregate_positive_negative([]),
            [],
        )

    def test_segregate_positive_negative_5(self):
        self.assertEqual(
            segregate_positive_negative([-1]),
            [-1],
        )

    def test_segregate_positive_negative_6(self):
        self.assertEqual(
            segregate_positive_negative([1]),
            [1],
        )

    def test_segregate_positive_negative_7(self):
        self.assertEqual(
            segregate_positive_negative([1, 2, 3, 4, 5]),
            [1, 2, 3, 4, 5],
        )


if __name__ == "__main__":
    unittest.main()
