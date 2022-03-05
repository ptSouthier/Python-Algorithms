def bubble_sort(list):
    has_swapped = True
    num_of_iterations = 0

    while has_swapped:
        has_swapped = False

        for index in range(len(list) - num_of_iterations - 1):
            if list[index] > list[index + 1]:
                list[index], list[index + 1] = list[index + 1], list[index]
                has_swapped = True

        num_of_iterations += 1

    return list


def is_anagram(first_string, second_string):
    string_a = bubble_sort(list(first_string))
    string_b = bubble_sort(list(second_string))

    return string_a == string_b
