from math import floor


def binary_search(sorted_li: list[int], target: int) -> int:
    head_pointer: int = sorted_li.index(sorted_li[0])
    tail_pointer: int = sorted_li.index(sorted_li[-1])
    middle_pointer: int = floor((head_pointer + tail_pointer) / 2)
    # print(middle_pointer)
    found: bool = False

    while not found:
        if target == sorted_li[middle_pointer]:
            return target

        if target == sorted_li[head_pointer]:
            return target

        if target == sorted_li[tail_pointer]:
            return target

        if sorted_li[middle_pointer] > target:
            tail_pointer = sorted_li[middle_pointer - 1]

        if sorted_li[middle_pointer] < target:
            head_pointer = sorted_li[middle_pointer + 1]


sorted_li: list[int] = [11, 14, 18, 20, 24, 25, 35, 39, 41, 44, 45, 48, 50]
print(binary_search(sorted_li, 35))
