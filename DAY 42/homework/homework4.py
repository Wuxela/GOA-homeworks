def high_and_low(numbers):
    num_list = numbers.split()
    num_list = [int(num) for num in num_list]
    highest = max(num_list)
    lowest = min(num_list)
    return f"{highest} {lowest}"