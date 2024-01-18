
# return Line[]
def read_calibration_input(filename = './calibration-input.txt'):
    lines = []
    with open(filename, 'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            lines.append(line)
    return lines

w2d_map = {
    "one": 'o1e',
    "two": 't2o',
    "three": 't3e',
    "four": 'f4r',
    "five": 'f5e',
    "six": 's6x',
    "seven": 's7n',
    "eight": 'e8t',
    "nine": 'n9n'
}


def words_to_digits(line):
    for key, value in w2d_map.items():
        check_past_index = 0
        try:
            while True: # will continue to replace digits until none found
                print('check past', check_past_index)
                print('check for ', key, 'in', line[check_past_index:])
                index = line[check_past_index:].index(key)
                print('found at', index)
                new_check_past_value = index + 1 + len(value) + check_past_index
                line = line[:check_past_index] + line[check_past_index:index] + value + line[index:] 
                check_past_index = new_check_past_value
                print('new line', line)
        except ValueError:
            continue
        except IndexError:
            continue

    return line

def get_next_digit(s, first_index):
    for i in range(len(s) - first_index):
        next_char = s[i + first_index]
        if is_int(next_char):
            return [int(next_char), i + first_index]
        else:
            continue
    return [None, len(s)]


def read_calibration_line(line: str):
    current_index = 0
    first_digit = None
    last_digit = None

    while current_index < len(line):
        [next_digit, last_index_checked] = get_next_digit(line, current_index)
        current_index = last_index_checked + 1
        if first_digit == None:
            first_digit = next_digit
            last_digit = next_digit
        elif next_digit != None:
            last_digit = next_digit

    return [first_digit, last_digit]

def is_int(c):
    try:
        int(c)
        return True
    except ValueError:
        return False


lines = read_calibration_input()
sum = 0
for i in range(0): 
    print(lines[i])
    line = words_to_digits(lines[i])
    print('  replaced:', line)
    digits = read_calibration_line(line)
    print('  digits:', digits)
    number = digits[0] * 10 + digits[1]
    print('  number:', number)
    sum += number

print('sum', sum)

d = words_to_digits('sxoneightoneckk9ldctxxnffqnzmjqvj')
print('d', d)




# I misunderstood the problem
def get_next_int(s, first_index):
    print('get next int for ', s, 'starting at ', first_index, 'i.e.', s[first_index:])
    current_int = None

    for i in range(len(s) - first_index):
        print(i, s[i + first_index])
        next_char = s[i + first_index]
        is_char_int = is_int(next_char)
        print('ici', is_char_int)

        if is_char_int:
            if current_int == None:
                current_int = int(next_char)
            else:
                current_int = current_int * 10 + int(next_char)
        else:
            if current_int == None:
                current_int = None
                continue
            else:
                return [current_int, i]

    return [current_int, len(s)] ## did not fint int, all positions
