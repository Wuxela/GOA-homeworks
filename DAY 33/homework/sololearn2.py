def remove_first_and_last(text):
    if len(text) <= 2:
        return ""
    return text[1:-1]