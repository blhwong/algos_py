def normalize_pattern(pattern):
    if pattern[0] == 'x':
        return False, pattern
    return True, ['x' if char == 'y' else 'y' for char in pattern]

def get_string(x, y, pattern):
    string = ''
    for char in pattern:
        if char == 'x':
            string += x
        else:
            string += y
    return string

def patternMatcher(pattern, string):
    swapped, normalized_pattern = normalize_pattern(pattern)
    table = { 'x': [], 'y': [] }
    for i, char in enumerate(normalized_pattern):
        char = normalized_pattern[i]
        table[char].append(i)

    total_len = len(string)
    if table['y']:
        for len_of_x in range(1, total_len):
            len_of_y = (total_len - len(table['x']) * len_of_x) // len(table['y'])
            x = string[:len_of_x]
            y_start = len_of_x * table['y'][0]
            y = string[y_start:y_start+len_of_y]
            s = get_string(x, y, normalized_pattern)
            if s == string:
                return [x, y] if not swapped else [y, x]
    else:
        len_of_x = total_len // len(table['x'])
        x = string[:len_of_x]
        return [x, ''] if not swapped else ['', x]

    return []
