def find_kth_largest_el(array, k):
    if k <= 0 or k > len(array):
        return None

    k_pos_el = len(array) - k
    array_and_indexes = [(val, idx) for idx, val in enumerate(array)]
    
    result = quick_select(array_and_indexes, 0, len(array) - 1, k_pos_el)
    return result[0], result[1]

    
def quick_select(array_and_indexes, left, right, k_pos_el):
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
        return quick_select(array_and_indexes, left, cursor - 1, k_pos_el)
    elif cursor < k_pos_el:
        return quick_select(array_and_indexes, cursor + 1, right, k_pos_el)
    else:
        return array_and_indexes[k_pos_el][0], array_and_indexes[k_pos_el][1]
