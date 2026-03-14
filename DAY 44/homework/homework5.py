def countChar(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count