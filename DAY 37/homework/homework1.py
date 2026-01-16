def count_char_occurrences(input_string, char_to_count):
    count = 0
    for char in input_string:
        if char == char_to_count:
            count += 1
    return count