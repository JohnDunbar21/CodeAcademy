love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

def lines_stripped(input_list):
    new_list = []
    for item in input_list:
        new = item.strip()
        new_list.append(new)
    return new_list


love_maybe_lines_stripped = lines_stripped(love_maybe_lines)

print(love_maybe_lines_stripped)

love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)