from typing import List


def max_jump(track: List[int]) -> bool:
    """You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

        false

        Return: true if you can reach the last index, or

        otherwise"""

    size = len(track) - 1
    i = 0

    while i <= size:
        if i == size:
            return True
        i += track[i]
    return False
