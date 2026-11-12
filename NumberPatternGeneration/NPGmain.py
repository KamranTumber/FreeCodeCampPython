def number_pattern(n):
    # 1. Check if n is an integer (and not a boolean like True/False)
    if not isinstance(n, int) or isinstance(n, bool):
        return "Argument must be an integer value."
    
    # 2. Check if n is less than 1
    if n < 1:
        return "Argument must be an integer greater than 0."
    
    # 3. Build the pattern using a for loop without a trailing space
    pattern = ""
    for i in range(1, n + 1):
        if i == 1:
            pattern += str(i)
        else:
            pattern += " " + str(i)
            
    return pattern