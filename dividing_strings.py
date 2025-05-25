import unittest


def dividing_string(string: str):
    s, e = "", ""
    str_len = len(string)
    med_index = str_len // 2 - 1 if str_len % 2 == 0 else str_len // 2
    s, e = string[: med_index + 1], string[med_index + 1 :]
    print(f"dividing_string('{string}') -> ('{s}', '{e}')")  # For debugging
    return s, e


def dividing_strings(*strings):
    s, e = "", ""
    for string in strings:
        a, b = dividing_string(string)
        s, e = s + a, e + b
    return s, e


class TestDividingStrings(unittest.TestCase):
    def test_no_strings(self):
        """Tests dividing_strings with no input strings."""
        self.assertEqual(dividing_strings(), ("", ""), "Test Failed: No strings")

    def test_single_empty_string(self):
        """Tests dividing_strings with a single empty string."""
        self.assertEqual(
            dividing_strings(""), ("", ""), "Test Failed: Single empty string"
        )

    def test_single_character_string(self):
        """Tests dividing_strings with a single character string."""
        # dividing_string("a") -> ("a", "")
        self.assertEqual(
            dividing_strings("a"),
            ("a", ""),
            "Test Failed: Single character string",
        )

    def test_single_even_length_string(self):
        """Tests dividing_strings with a single string of even length."""
        # dividing_string("test") -> ("te", "st")
        self.assertEqual(
            dividing_strings("test"),
            ("te", "st"),
            "Test Failed: Single even length string",
        )

    def test_single_odd_length_string(self):
        """Tests dividing_strings with a single string of odd length."""
        # dividing_string("hello") -> ("hel", "lo")
        self.assertEqual(
            dividing_strings("hello"),
            ("hel", "lo"),
            "Test Failed: Single odd length string",
        )

    def test_multiple_strings_varied_lengths(self):
        """Tests dividing_strings with multiple strings of different lengths."""
        # "abcd" -> ("ab", "cd")
        # "e"    -> ("e", "")
        # "fghij"-> ("fgh", "ij")
        # Result: s_agg = "ab" + "e" + "fgh" = "abefgh"
        #         e_agg = "cd" + "" + "ij"  = "cdij"
        self.assertEqual(
            dividing_strings("abcd", "e", "fghij"),
            ("abefgh", "cdij"),
            "Test Failed: Multiple strings of varied lengths",
        )

    def test_multiple_strings_with_empty_string(self):
        """Tests dividing_strings with multiple strings including an empty one."""
        # "AB"  -> ("A", "B")
        # ""    -> ("", "")
        # "CDE" -> ("CD", "E")
        # Result: s_agg = "A" + "" + "CD" = "ACD"
        #         e_agg = "B" + "" + "E"  = "BE"
        self.assertEqual(
            dividing_strings("AB", "", "CDE"),
            ("ACD", "BE"),
            "Test Failed: Multiple strings with an empty string",
        )

    def test_strings_resulting_in_empty_second_parts(self):
        """Tests dividing_strings where individual strings result in empty second parts."""
        # "x" -> ("x", "")
        # "y" -> ("y", "")
        # Result: s_agg = "x" + "y" = "xy"
        #         e_agg = "" + "" = ""
        self.assertEqual(
            dividing_strings("x", "y"),
            ("xy", ""),
            "Test Failed: Strings resulting in empty second parts",
        )

    def test_mix_of_short_strings(self):
        """Tests dividing_strings with a mix of various short strings."""
        """
        Tests the dividing_strings function with various inputs.
        """
        # "hi" -> ("h", "i")
        # "j"  -> ("j", "")
        # "klm"-> ("kl", "m")
        # Result: s_agg = "h" + "j" + "kl" = "hjkl"
        #         e_agg = "i" + "" + "m"  = "im"
        self.assertEqual(
            dividing_strings("hi", "j", "klm"),
            ("hjkl", "im"),
            "Test Failed: Mix of short strings",
        )


if __name__ == "__main__":
    unittest.main()
