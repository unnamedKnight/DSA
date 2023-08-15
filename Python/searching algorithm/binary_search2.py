def binary_search(sorted_li: list[int], target: int) -> int:
    left = 0
    right = len(sorted_li) - 1

    while left <= right:
        middle = (left + right) // 2
        if target == sorted_li[middle]:
            return middle

        elif target > sorted_li[middle]:
            left = middle + 1

        else:
            right = middle - 1


sorted_li: list[int] = [11, 14, 18, 20, 24, 25, 35, 39, 41, 44, 45, 48, 50]

print(binary_search(sorted_li, 25))
