import unittest
from lengthOfLongestSubstring import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "abcabcbb"
        self.assertEqual(3, Solution().lengthOfLongestSubstring(s))

    def test_2(self):
        s = "bbbbb"
        self.assertEqual(1, Solution().lengthOfLongestSubstring(s))

    def test_3(self):
        s = "pwwkew"
        self.assertEqual(3, Solution().lengthOfLongestSubstring(s))

    def test_4(self):
        s = ""
        self.assertEqual(0, Solution().lengthOfLongestSubstring(s))

    def test_5(self):
        s = " "
        self.assertEqual(1, Solution().lengthOfLongestSubstring(s))

    def test_6(self):
        s = "dvdf"
        self.assertEqual(3, Solution().lengthOfLongestSubstring(s))
