def merge_sort(my_arr: list[int]):
    if len(my_arr) == 1:
        return my_arr

    middle: int = len(my_arr) // 2
    right: list[int] = my_arr[:middle]
    left: list[int] = my_arr[middle:]

    left_result = merge_sort(left)
    right_result = merge_sort(right)

    return merge(left_result, right_result)


def merge(left_result, right_result):
    result = [None] * (len(left_result) + len(right_result))
    i = j = k = 0

    while i < len(left_result) and j < len(right_result):
        if left_result[i] < right_result[j]:
            result[k] = left_result[i]
            # result.append(left_result[i])
            i += 1
        else:
            result[k] = right_result[j]
            # result.append(right_result[j])
            j += 1

        k += 1

    while i < len(left_result):
        result[k] = left_result[i]
        k += 1
        i += 1

    while j < len(right_result):
        result[k] = right_result[j]
        k += 1
        j += 1

    return result


print(merge_sort([3, 1, 4, 2]))
