import unittest


def unique_list(arr: list):
    # return list(set(arr))
    return list(dict.fromkeys(arr))


def unique_list_adjacent(arr: list):
    unique_list = []
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i - 1]:
            unique_list.append(arr[i])
    return unique_list


class TestUniqueListFunctions(unittest.TestCase):

    # Tests for unique_list function
    def test_unique_list_empty(self):
        """Test unique_list with an empty list."""
        self.assertEqual(unique_list([]), [])

    def test_unique_list_all_unique(self):
        """Test unique_list with a list of all unique elements."""
        self.assertEqual(unique_list([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_unique_list_with_duplicates(self):
        """Test unique_list with duplicate elements, preserving first appearance order."""
        self.assertEqual(unique_list([1, 2, 2, 3, 4, 1, 5]), [1, 2, 3, 4, 5])

    def test_unique_list_with_duplicates_at_ends(self):
        """Test unique_list with duplicates at the beginning and end."""
        self.assertEqual(unique_list([1, 1, 2, 3, 3]), [1, 2, 3])

    def test_unique_list_mixed_types(self):
        """Test unique_list with mixed data types."""
        self.assertEqual(unique_list([1, "a", 1, "b", "a", 2]), [1, "a", "b", 2])

    def test_unique_list_with_none(self):
        """Test unique_list with None values."""
        self.assertEqual(unique_list([1, None, 2, None, 1]), [1, None, 2])

    # Tests for unique_list_adjacent function
    def test_unique_list_adjacent_empty(self):
        """Test unique_list_adjacent with an empty list."""
        self.assertEqual(unique_list_adjacent([]), [])

    def test_unique_list_adjacent_no_adjacent_duplicates(self):
        """Test unique_list_adjacent with no adjacent duplicates."""
        self.assertEqual(unique_list_adjacent([1, 2, 3, 1, 4]), [1, 2, 3, 1, 4])

    def test_unique_list_adjacent_simple_duplicates(self):
        """Test unique_list_adjacent with simple adjacent duplicates."""
        self.assertEqual(unique_list_adjacent([1, 1, 2, 3, 3, 3, 4]), [1, 2, 3, 4])

    def test_unique_list_adjacent_duplicates_at_start(self):
        """Test unique_list_adjacent with duplicates at the start."""
        self.assertEqual(unique_list_adjacent([1, 1, 1, 2, 3]), [1, 2, 3])

    def test_unique_list_adjacent_duplicates_at_end(self):
        """Test unique_list_adjacent with duplicates at the end."""
        self.assertEqual(unique_list_adjacent([1, 2, 3, 3, 3]), [1, 2, 3])

    def test_unique_list_adjacent_multiple_groups(self):
        """Test unique_list_adjacent with multiple groups of adjacent duplicates."""
        self.assertEqual(
            unique_list_adjacent([1, 1, 2, 2, 1, 3, 3, 3, 2, 2]), [1, 2, 1, 3, 2]
        )

    def test_unique_list_adjacent_all_same_elements(self):
        """Test unique_list_adjacent with all elements being the same."""
        self.assertEqual(unique_list_adjacent([5, 5, 5, 5, 5]), [5])

    def test_unique_list_adjacent_mixed_types(self):
        """Test unique_list_adjacent with mixed data types and adjacent duplicates."""
        self.assertEqual(
            unique_list_adjacent([1, 1, "a", "a", 1, "b", "b", "a"]),
            [1, "a", 1, "b", "a"],
        )

    def test_unique_list_adjacent_with_none(self):
        """Test unique_list_adjacent with None values and adjacent duplicates."""
        self.assertEqual(
            unique_list_adjacent([1, None, None, 2, None, 1, 1]), [1, None, 2, None, 1]
        )


if __name__ == "__main__":
    unittest.main()
