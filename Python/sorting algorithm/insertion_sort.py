def insertion_sort(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        key = arr[i]
        last = i - 1
        while last >= 0 and key < arr[last]:
            arr[last + 1] = arr[last]
            last -= 1
        arr[last + 1] = key


arr = [32, 34, 11, 96, 0, 25]
insertion_sort(arr)
print(arr)
