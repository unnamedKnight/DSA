# def quicksort(my_array):
#     quicksort_helper(my_array, 0, len(my_array) - 1)
#     return my_array


# def quicksort_helper(arr, start, end):
#     if start >= end:
#         return
#     pivot = start
#     left = start + 1
#     right = end
#     while right >= left:
#         if arr[left] > arr[pivot] and arr[right] < arr[pivot]:
#             arr[left], arr[right] = arr[right], arr[left]

#         if arr[left] <= arr[pivot]:
#             left += 1

#         if arr[right] >= arr[pivot]:
#             # print(f'Inside arr[right] condition: {arr}')
#             right -= 1


#     arr[pivot], arr[right] = arr[right], arr[pivot]

#     quicksort_helper(arr, start, right - 1)

#     quicksort_helper(arr, right + 1, end)


def quicksort(my_arr):
    quicksort_helper(my_arr, 0, len(my_arr) - 1)
    return my_arr


def quicksort_helper(my_arr, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while right >= left:
        if my_arr[left] > my_arr[pivot] and my_arr[right] < my_arr[pivot]:
            my_arr[left], my_arr[right] = my_arr[right], my_arr[left]

        if my_arr[left] <= my_arr[pivot]:
            left += 1

        if my_arr[right] >= my_arr[pivot]:
            right -= 1

    my_arr[pivot], my_arr[right] = my_arr[right], my_arr[pivot]

    quicksort_helper(my_arr, start, right - 1)
    quicksort_helper(my_arr, right + 1, end)


my_arr = [4, 1, 3, 7, 2, 6, 5]
print(quicksort(my_arr))
# quicksort(my_arr)
