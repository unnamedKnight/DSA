def quicksort(arr):
    quicksort_helper(arr, 0, len(arr) - 1)
    return arr


def quicksort_helper(arr, start, end):
    if start > end:
        return
    pivot = start
    right = start + 1
    left = end

    while right >= left:
        if arr[left] > arr[pivot] and arr[right] < arr[pivot]:
            arr[left], arr[right] = arr[right], arr[left]

        if arr[left] <= arr[pivot]:
            left += 1

        if arr[right] >= arr[pivot]:
            right -= 1

    arr[pivot], arr[right] = arr[right], arr[pivot]

    quicksort_helper(arr, start, right - 1)
    quicksort_helper(arr, start, right + 1)


print(quicksort([4, 5, 1, 6, 7, 2]))
