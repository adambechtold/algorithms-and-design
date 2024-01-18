import unittest

def read_input(filename = 'input.txt'):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]


print('======== PART 1 ========')

def print_matrix(matrix):
    for line in matrix:
        print(line)


'''
type Point
    x: number
    y: number
    value: string
'''


# Input MxN matrix
# return Point[] 
def neighbors(matrix, x, y):

    max_y = len(matrix) - 1
    max_x = len(matrix[0]) - 1

    n = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            #print('i', i, 'j', j)
            if i == x and j == y:
                #   print('skipping...')
                #print('i:', i, 'j:', j, 'value:', matrix[j][i])
                continue
            if i <= max_x and j <= max_y and i >= 0 and j >= 0:
                # print('value at ', j, i, 'is', matrix[j][i])
                n.append({
                    'x': i,
                    'y': j,
                    'value': matrix[j][i]
                })
    return n


print('- - - - Test: neighbors - - - -')
class TestNeighbors(unittest.TestCase):
    def test_complex_matrix(self):
        complex_matrix = ['abcdefg', 'hijklmn', 'opqrstu']
        expected_values = ['h', 'b', 'i']
        ns = neighbors(complex_matrix, 0,0)
        self.assertCountEqual([neighbor['value'] for neighbor in ns], expected_values)

        expected_values = ['t', 'm', 'n']
        last_x = len(complex_matrix[0]) - 1
        last_y = len(complex_matrix) - 1
        ns = neighbors(complex_matrix, len(complex_matrix[0]) - 1, len(complex_matrix) - 1)
        self.assertCountEqual([neighbor['value'] for neighbor in ns], expected_values)

        expected_values = ['i', 'k', 'b', 'c', 'd', 'p', 'q', 'r']
        ns = neighbors(complex_matrix, 2, 1)
        self.assertCountEqual([neighbor['value'] for neighbor in ns], expected_values)

    def test_empty_matrix(self):
        empty_matrix = [[]]
        self.assertEqual(neighbors(empty_matrix, 0, 0), [])
        self.assertEqual(neighbors(empty_matrix, 100, 100), [])

    def test_simple_matrix(self):
        simple_matrix = ['ab', 'cd']
        expected_values = ['b', 'c', 'd']
        n = neighbors(simple_matrix, 0, 0)
        self.assertCountEqual([neighbor['value'] for neighbor in n], expected_values)

        n = neighbors(simple_matrix, 1,1)
        expected_values = ['a', 'b', 'c']
        self.assertCountEqual([neighbor['value'] for neighbor in n], expected_values)


def find_symbols(matrix):
    symbol_points = []
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if is_symbol(matrix[y][x]):
                symbol_points.append({
                    'x': x,
                    'y': y,
                    'value': matrix[y][x]
                })
    return symbol_points

class TestFindSymbols(unittest.TestCase):
    def tests(self):
        simple_matrix = ['2.', '#1']
        locations = find_symbols(simple_matrix)
        self.assertEqual(len(locations) , 1)
        self.assertEqual(locations[0]['x'], 0)
        self.assertEqual(locations[0]['y'], 1)

        complex_matrix = [
            '12...231#', 
            '&..*..23.',
            '.123.!...'
        ]
        locations = find_symbols(complex_matrix)
        self.assertEqual(len(locations), 4)

def is_symbol(s):
    try:
        int(s)
        return False
    except ValueError:
        return s != '.'

class TestIsSymbol(unittest.TestCase):
    def tests(self):
        self.assertEqual(is_symbol('9'), False)
        self.assertEqual(is_symbol('.'), False)
        self.assertEqual(is_symbol('a'), True)
        self.assertEqual(is_symbol('!'), True)
        self.assertEqual(is_symbol('$'), True)
        self.assertEqual(is_symbol('#'), True)
        self.assertEqual(is_symbol('*'), True)

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    

def replace_char_at_index(string, index, new_char):
    if 0 <= index < len(string):
        return string[:index] + new_char + string[index+1:]
    else:
        return string

def read_and_replace_neighbor_numbers(matrix, locations):
    max_x = len(matrix[0]) - 1
    sample_numbers = []
    for l in locations:
        ns = neighbors(matrix, l['x'], l['y'])
        for n in ns:
            try:
                value = int(matrix[n['y']][n['x']])
                matrix[n['y']] = replace_char_at_index(matrix[n['y']], n['x'], 'x')
                # go right
                for i in range(n['x'] + 1, max_x + 1):
                    target_value = matrix[n['y']][i]
                    if is_int(target_value):
                        value = value * 10 + int(target_value)
                        matrix[n['y']] = replace_char_at_index(matrix[n['y']], i, 'x')
                    else:
                        break
                for i in range(n['x'] - 1, -1, -1):
                    target_value = matrix[n['y']][i]
                    if is_int(target_value):
                        value = value + int(target_value) * 10 * len(str(value))
                        matrix[n['y']] = replace_char_at_index(matrix[n['y']], i, 'x')
                    else:
                        break
                sample_numbers.append(value)
            except ValueError:
                continue
    return sample_numbers


class TestReadAndReplace(unittest.TestCase):
    def test_simple(self):
        simple_matrix = ['1.', '*.']
        locations = find_symbols(simple_matrix)
        sample_numbers = read_and_replace_neighbor_numbers(simple_matrix, locations)
        self.assertCountEqual(sample_numbers, [1])

    def test_complex(self):
        complex_matrix = [
            '123...#',
            '121....',
            '9&...21',
            '*....*.'
        ]
        locations = find_symbols(complex_matrix)
        sample_numbers = read_and_replace_neighbor_numbers(complex_matrix, locations)
        self.assertCountEqual(sample_numbers, [121,9,21])

#unittest.main()

print('------- EXAMPLE --------')
test_lines = read_input('test-input.txt')
for line in test_lines:
    print(line)

#print(neighbors(test_lines, 0,0))
print(find_symbols(test_lines))
symbol_locations = find_symbols(test_lines)

sample_numbers = read_and_replace_neighbor_numbers(test_lines, symbol_locations)
print('new state', print_matrix(test_lines))
print(sample_numbers)
print('sum:', sum(sample_numbers))



