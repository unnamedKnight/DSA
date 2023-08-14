from math import floor


def binary_search(sorted_li: list[int], target: int) -> int:
    head_pointer: int = sorted_li.index(sorted_li[0])
    tail_pointer: int = sorted_li.index(sorted_li[-1])
    middle_pointer: int = floor((head_pointer + tail_pointer) / 2)
    # print(middle_pointer)
    found: bool = False
    cycle_count: int = 0

    print('Cycle Starts')
    while not found:
        cycle_count += 1
        print(f"Cycle Count: {cycle_count}")
        print(f'tail_pointer*******: {tail_pointer}')
        print(f'head pointer: {sorted_li[head_pointer]}')
        print(f'middle pointer: {sorted_li[middle_pointer]}')
        print(f'tail pointer: {sorted_li[tail_pointer]}')
        print(f'target: {target}')
        if target == sorted_li[middle_pointer]:
            return target

        elif target == sorted_li[head_pointer]:
            return target

        elif target == sorted_li[tail_pointer]:
            return target

        if sorted_li[middle_pointer] > target:
            tail_pointer = sorted_li.index(sorted_li[middle_pointer - 1])
            middle_pointer = floor((head_pointer + tail_pointer) / 2)


        elif sorted_li[middle_pointer] < target:
            head_pointer = sorted_li.index(sorted_li[middle_pointer + 1])
            middle_pointer = floor((head_pointer + tail_pointer) / 2)


        # if cycle_count >= 5:
        #     break
        # print('\n')


sorted_li: list[int] = [11, 14, 18, 20, 24, 25, 35, 39, 41, 44, 45, 48, 50]
# print(binary_search(sorted_li, 35))

binary_search(sorted_li, 14)
