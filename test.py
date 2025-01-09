def romanToInt(s):
    """
    :type s: str
    """
    # prev = 0
    converted = 0
    store = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    l = len(s)
    i = 0
    while i < l:
        try:
            if store[s[i + 1]] > store[s[i]]:
                i += 2
                converted += store[s[i -1]] - store[s[i - 2]]
                # print("works", converted)
                continue
        except IndexError:
            pass
            # print("error")
        converted += store[s[i]]
        i += 1
    return converted


if __name__ == "__main__":
    nums: int = "MCMXCIV"
    print(romanToInt(nums))
    # romanToInt(nums)
