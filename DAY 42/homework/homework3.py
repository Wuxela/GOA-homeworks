def get_count(input_str):
    vowels = 'aeiou'    
    count = 0
    for char in input_str:
        if char in vowels:
            count += 1
    return count