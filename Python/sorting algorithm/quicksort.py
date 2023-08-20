def quicksort(my_array):
    quicksort_helper(my_array, 0, len(my_array) - 1)
    return my_array


def quicksort_helper(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while right >= left:
        if arr[left] > arr[pivot] and arr[right] < arr[pivot]:
            print(f'Inside and condition: {arr}')
            arr[left], arr[right] = arr[right], arr[left]

        if arr[left] <= arr[pivot]:
            left += 1
            print(arr)

        if arr[right] >= arr[pivot]:
            right -= 1

    print(f'value of right: {right}')
    arr[pivot], arr[right] = arr[right], arr[pivot]

    quicksort_helper(arr, start, right - 1)
    quicksort_helper(arr, right + 1, end)


my_arr = [1, 3, 2, 5, 4]
# print(quicksort(my_arr))
quicksort(my_arr)
