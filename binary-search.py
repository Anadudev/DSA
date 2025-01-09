def binary_search(array, search: int):
    left = 0
    right = len(array) - 1
    mid = 0

    while left <= right:
        # print(mid)
        mid = (left + right) // 2
        if array[mid] < search:
            left = mid + 1
        elif array[mid] > search:
            right = mid - 1
        else:
            return mid
    return -1


if __name__ == "__main__":

    binary = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    search = 1
    print(binary_search(binary, search))
