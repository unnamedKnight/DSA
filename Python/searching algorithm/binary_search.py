def binary_search(sorted_li: list[int], target: int) -> int:
    left_pointer: int = 0
    right_pointer: int = len(sorted_li) - 1

    while left_pointer <= right_pointer:
        middle_pointer: int = (left_pointer + right_pointer) // 2

        if target in [
            sorted_li[middle_pointer],
            sorted_li[left_pointer],
            sorted_li[right_pointer],
        ]:
            return middle_pointer

        if sorted_li[middle_pointer] > target:
            right_pointer = middle_pointer - 1
        elif sorted_li[middle_pointer] < target:
            left_pointer = middle_pointer + 1


sorted_li: list[int] = [11, 14, 18, 20, 24, 25, 35, 39, 41, 44, 45, 48, 50]
print(binary_search(sorted_li, 44))
