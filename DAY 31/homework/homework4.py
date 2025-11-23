def filter_long_names(names):
    long_names = []
    
    for name in names:
        if len(name) >= 5:
            long_names.append(name)
    
    return long_names