def find_kth_largest_el(array, k):
    if k <= 0 or k > len(array):
        return None

    k_pos_el = len(array) - k
    array_and_indexes = [(val, idx) for idx, val in enumerate(array)]

    def quick_select(left, right):
        pivot = array_and_indexes[right][0]

        cursor = left

        for i in range(left, right):
            if array_and_indexes[i][0] <= pivot:
                array_and_indexes[i], array_and_indexes[cursor] = (
                    array_and_indexes[cursor],
                    array_and_indexes[i],
                )
                cursor += 1

        array_and_indexes[right], array_and_indexes[cursor] = (
            array_and_indexes[cursor],
            array_and_indexes[right],
        )

        if cursor > k_pos_el:
            return quick_select(left, cursor - 1)
        elif cursor < k_pos_el:
            return quick_select(cursor + 1, right)
        else:
            return array_and_indexes[k_pos_el][0], array_and_indexes[k_pos_el][1]

    result = quick_select(0, len(array) - 1)
    return result[0], result[1]


array_example = [15, 7, 22, 9, 36, 2, 42, 18]
k = 3
result, position = find_kth_largest_el(array_example, k)
print(f'Знайдений {k}-й найбільший елемент: {result}')
print(f'Позиція {k}-го найбільшого елемента в масиві: {position}')
