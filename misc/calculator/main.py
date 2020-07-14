def add(nums):
    ans = 0
    for num in nums:
        ans += int(num)

    return ans

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


    to_add = []
    to_subtract = []
    operation = '+' if cleaned_str[0] != '-' else '-'
    curr = ''
    for char in cleaned_str:
        if char == '+' or char == '-':
            if operation == '+':
                to_add.append(curr)
            elif operation == '-':
                to_subtract.append(f'-{curr}')
            operation = char
            curr = ''
        else:
            curr += char

    if operation == '+':
        to_add.append(curr)
    elif operation == '-':
        to_subtract.append(f'-{curr}')

    return add(to_add) + add(to_subtract)
