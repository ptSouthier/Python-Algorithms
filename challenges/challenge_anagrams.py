def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    left, right = merge_sort(list[:mid]), merge_sort(list[mid:])
    return merge(left, right, list.copy())


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


def is_anagram(first_string, second_string):
    string_a = merge_sort(list(first_string))
    string_b = merge_sort(list(second_string))
    return string_a == string_b
