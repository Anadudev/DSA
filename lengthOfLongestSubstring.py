class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s and isinstance(s, str) and len(s) > 0:
            if len(s) == 1:
                return 1
            tracker = {s[0]:s[0]}
            maximum = 0
            for character in s[1:]:
                if character in tracker:
                    size = len(tracker)
                    if maximum < size:
                        maximum = size
                    tracker = {}
                tracker[character] = character
            return maximum if maximum > len(tracker) else len(tracker)


if __name__ == "__main__":
    display = Solution()
    print(display.lengthOfLongestSubstring("dvdf"))
