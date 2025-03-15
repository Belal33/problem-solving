import unittest


class CharactersFreq:

    def __init__(self, text: str):
        self.text = text

    def ascii(self):
        chars_freq_by_Ascii_index = [
            0
        ] * 127  # each index represents an ASCII character code
        answer = dict()
        for char in self.text:
            char_i = ord(char)
            if char_i < 127:
                chars_freq_by_Ascii_index[char_i] += 1
        for i, n in enumerate(chars_freq_by_Ascii_index):
            if n > 0:

                answer[chr(i)] = n
        print(self.sort_dict(answer))
        return answer

    def merge_sort_kv_array(self, arr: list[tuple[str, int]]) -> list[tuple[str, int]]:
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.merge_sort_kv_array(arr[:mid])
        right = self.merge_sort_kv_array(arr[mid:])
        # start merging
        left_iter = iter(left)
        right_iter = iter(right)
        left_el = next(left_iter)
        right_el = next(right_iter)
        sorted_arr = []
        while True:

            if left_el[1] < right_el[1]:
                sorted_arr.append(left_el)
                left_el = next(left_iter, None)
                if left_el is None:
                    sorted_arr.append(right_el)
                    sorted_arr.extend(right_iter)
                    break
            else:
                sorted_arr.append(right_el)
                right_el = next(right_iter, None)
                if right_el is None:
                    sorted_arr.append(left_el)
                    sorted_arr.extend(left_iter)
                    break

        return sorted_arr

    def sort_dict(self, d: dict):
        dict_arr = [(k, v) for k, v in d.items()]
        answer = self.merge_sort_kv_array(dict_arr)
        return answer

    def UTF8(self):
        answer = dict()

        for char in self.text:
            if answer.get(char):
                answer[char] += 1
            else:
                answer[char] = 1
        print(self.sort_dict(answer))
        return answer


# create a test case
class TestCharactersFreqUTF8(unittest.TestCase):

    def test_UTF8_0(self):
        text = "Hello world!"
        cf = CharactersFreq(text)
        self.assertEqual(
            cf.UTF8(),
            {"H": 1, "e": 1, "l": 3, "o": 2, " ": 1, "w": 1, "r": 1, "d": 1, "!": 1},
        )

    def test_UTF8_empty_string(self):
        text = ""
        cf = CharactersFreq(text)
        self.assertEqual(
            cf.UTF8(),
            {},
        )

    def test_UTF8_repeted_random_char(self):
        text = " aaaaaa"
        cf = CharactersFreq(text)
        self.assertEqual(
            cf.UTF8(),
            {"a": 6, " ": 1},
        )

    def test_UTF8_special_characters(self):
        text = "!@#$%^&*()"
        cf = CharactersFreq(text)
        self.assertEqual(
            cf.UTF8(),
            {
                "!": 1,
                "@": 1,
                "#": 1,
                "$": 1,
                "%": 1,
                "^": 1,
                "&": 1,
                "*": 1,
                "(": 1,
                ")": 1,
            },
        )

    def test_UTF8_mixed_case(self):
        text = "AaBbCc"
        cf = CharactersFreq(text)
        self.assertEqual(
            cf.UTF8(),
            {"A": 1, "a": 1, "B": 1, "b": 1, "C": 1, "c": 1},
        )

    def test_UTF8_numbers(self):
        text = "1234567890"
        cf = CharactersFreq(text)
        self.assertEqual(
            cf.UTF8(),
            {
                "1": 1,
                "2": 1,
                "3": 1,
                "4": 1,
                "5": 1,
                "6": 1,
                "7": 1,
                "8": 1,
                "9": 1,
                "0": 1,
            },
        )

    def test_UTF8_unicode_characters(self):
        text = "こんにちは世界"  # "Hello World" in Japanese
        cf = CharactersFreq(text)
        self.assertEqual(
            cf.UTF8(),
            {"こ": 1, "ん": 1, "に": 1, "ち": 1, "は": 1, "世": 1, "界": 1},
        )


class TestCharactersFreqAscii(unittest.TestCase):

    def test_ascii_0(self):
        text = "Hello world!"
        cf = CharactersFreq(text)
        self.assertEqual(
            cf.ascii(),
            {"H": 1, "e": 1, "l": 3, "o": 2, " ": 1, "w": 1, "r": 1, "d": 1, "!": 1},
        )

    def test_ascii_empty_string(self):
        text = ""
        cf = CharactersFreq(text)
        self.assertEqual(
            cf.ascii(),
            {},
        )

    def test_ascii_repeted_random_char(self):
        text = " aaaaaa"
        cf = CharactersFreq(text)
        self.assertEqual(
            cf.ascii(),
            {"a": 6, " ": 1},
        )


if __name__ == "__main__":
    unittest.main()
