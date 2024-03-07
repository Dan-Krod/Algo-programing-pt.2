def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]

    left = [i for i in array if i < pivot]
    mid = [i for i in array if i == pivot]
    right = [i for i in array if i > pivot]
        
    return quick_sort(left) + mid + quick_sort(right)


def check_posibility_to_place_cow(free_sections, count_of_angry_cows, min_dist):
    position = free_sections[0]

    for section in free_sections[1:]:
        if section - position >= min_dist:
            count_of_angry_cows -= 1
            position = section

            if count_of_angry_cows == 1:
                return True

    return False


def largest_min_width(free_sections, angry_cows):
    sort_free_sections = quick_sort(free_sections)

    if angry_cows == 2:
        return sort_free_sections[-1] - sort_free_sections[0]
    
    if angry_cows < 2 or angry_cows > 100000:
        return None

    min_dist = 1
    max_dist = sort_free_sections[-1] - sort_free_sections[0]

    while min_dist <= max_dist:
        mid_dist = min_dist + (max_dist - min_dist) // 2
        if check_posibility_to_place_cow(sort_free_sections, angry_cows, mid_dist):
            min_dist = mid_dist + 1
        else:
            max_dist = mid_dist - 1

    return max_dist


free_section = [0, 3, 4, 7, 10, 9]
C = 3
width_1 = largest_min_width(free_section, C)
print(f"The largest possible minimum distance is - {width_1}")

free_section = [1, 2, 8, 4, 9]
C = 3
width_2 = largest_min_width(free_section, C)
print(f"The largest possible minimum distance is - {width_2}")
