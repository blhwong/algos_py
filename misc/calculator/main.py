def calculate(input_string):
    cleaned_str = ''
    i = 0
    while i < len(input_string):
        char = input_string[i]
        if char == '(':
            opened = 1
            closed = 0
            j = i + 1
            inside = ''
            while j < len(input_string) and opened > closed:
                if input_string[j] == '(':
                    opened += 1
                elif input_string[j] == ')':
                    closed += 1

                inside += input_string[j]
                j += 1

            res = calculate(inside[:-1])
            if res < 0:
                cleaned_str = cleaned_str[:-1] + str(res)
            else:
                cleaned_str += str(res)
            i = j
        elif char != ')':
            cleaned_str += char
            i += 1


    starts_with_sign = cleaned_str[0] == '-' or cleaned_str[0] == '+'
    ans = 0
    start = 0 if not starts_with_sign else 1
    operation = '+' if not starts_with_sign else cleaned_str[0]
    curr = ''
    for i in range(start, len(cleaned_str)):
        char = cleaned_str[i]
        if char == '+' or char == '-':
            if operation == '+':
                ans += int(curr)
            elif operation == '-':
                ans -= int(curr)
            operation = char
            curr = ''
        else:
            curr += char

    if operation == '+':
        ans += int(curr)
    elif operation == '-':
        ans -= int(curr)

    return ans
