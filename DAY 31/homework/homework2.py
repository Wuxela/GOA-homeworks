def filter_positive_negative(numbers):
    positive_numbers = []
    negative_numbers = []
    
    for number in numbers:
        if number >= 0:
            positive_numbers.append(number)
        else:
            negative_numbers.append(number)
    
    return positive_numbers, negative_numbers