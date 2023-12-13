import unittest
from dataclasses import dataclass
from typing import List, Set
from itertools import combinations


def read_input(filename = 'input.txt'):
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    return [l.strip() for l in lines]

@dataclass 
class Coordinates:
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))

@dataclass
class Universe:
    image: List[str]
    galaxies: Set[Coordinates]


def parse_universe(lines: List[str]) -> Universe:
    image = []
    galaxies = set([])
    for row_index, line in enumerate(lines):
        row = [c for c in line]
        for i in range(len(row)):
            if row[i] == '#':
                c = Coordinates(i, row_index)
                galaxies.add(c)
        image.append(''.join(row))
    return Universe(image, galaxies)

class TestReadInput(unittest.TestCase):
    def testSimpleImage(self):
        example_image_file = 'simple-test-image.txt'
        lines = read_input(example_image_file)
        self.assertEqual(lines, ['.#', '#.'])
        
class TestParseInput(unittest.TestCase):
    def testSimpleUniverse(self):
        lines = [
            '.#',
            '#.'
        ]
        parsed_universe = parse_universe(lines)
        self.assertEqual(parsed_universe.image, ['.#', '#.'])
        self.assertEqual(len(parsed_universe.galaxies), 2)
        self.assertEqual(parsed_universe.galaxies, set([
            Coordinates(1,0),
            Coordinates(0,1)
        ]))
        lines = ['.#.']
        self.assertEqual(parse_universe(lines).image, ['.#.'])
        self.assertEqual(len(parse_universe(lines).galaxies), 1)
        self.assertEqual(parse_universe(lines).galaxies, set([
            Coordinates(1,0)
        ]))

def get_expanded_universe(universe: Universe) -> Universe:
    # track all columns
    [empty_rows, empty_columns] = find_empty_rows_and_columns(universe)

    list_of_empty_rows = list(empty_rows)
    list_of_empty_rows.sort(reverse=True)
    for r in list_of_empty_rows:
        universe_width = len(universe.image[0])
        new_matrix = insert_element_at_index(universe.image, '.' * universe_width, r + 1)
        universe.image = insert_element_at_index(universe.image, '.' * universe_width, r + 1)

    list_of_empty_columns = list(empty_columns)
    list_of_empty_columns.sort(reverse=True)
    for c in list_of_empty_columns:
        for r in range(len(universe.image)):
            universe.image[r] = universe.image[r][:c] + '.' + universe.image[r][c:]

    return parse_universe(universe.image) 


class TestGetExpandedUniverse(unittest.TestCase):
    def testExpandSimpleUniverse(self):
        lines = [
            '.'
        ]
        universe = parse_universe(lines)
        universe = get_expanded_universe(universe)
        self.assertEqual(universe.image, [
            '..',
            '..'
        ])
        lines = ['#']
        universe = parse_universe(lines)
        universe = get_expanded_universe(universe)
        self.assertEqual(universe.image, [
            '#',
        ])

    def testComplexUniverse(self):
        lines = [
            '.#.',
            '..#',
            '...'
        ]
        universe = parse_universe(lines)
        universe = get_expanded_universe(universe)
        self.assertEqual(universe.image, [
            '..#.',
            '...#',
            '....',
            '....'
        ])
        self.assertEqual(universe.galaxies, set([
            Coordinates(2,0),
            Coordinates(3,1)
        ]))

    def testExampleUniverse(self): 
        lines = [
            '...#......',
			'.......#..',
			'#.........',
			'..........',
			'......#...',
			'.#........',
			'.........#',
			'..........',
			'.......#..',
			'#...#.....'
        ]
        universe = parse_universe(lines)
        universe = get_expanded_universe(universe)
        self.assertEqual(universe.image, [
			'....#........',
			'.........#...',
			'#............',
			'.............',
			'.............',
			'........#....',
			'.#...........',
			'............#',
			'.............',
			'.............',
			'.........#...',
			'#....#.......'
        ])
        self.assertEqual(universe.galaxies, set([
            Coordinates(4,0),
            Coordinates(9,1),
            Coordinates(0,2),
            Coordinates(8,5),
            Coordinates(1,6),
            Coordinates(12,7),
            Coordinates(9,10),
            Coordinates(0,11),
            Coordinates(5,11)
        ]))


def find_empty_rows_and_columns(universe: Universe):
    empty_columns = set(range(len(universe.image[0])))
    empty_rows = set(range(len(universe.image)))
    for r in range(len(universe.image)):
        for c in range(len(universe.image[0])):
            if universe.image[r][c] != '.':
                empty_rows.discard(r)
                empty_columns.discard(c)
    return [empty_rows, empty_columns]


class TestFindEmptyRowsAndColumns(unittest.TestCase):
    def testUnitUniverse(self):
        universe = parse_universe(['.'])
        [empty_rows, empty_columns] = find_empty_rows_and_columns(universe)
        self.assertEqual(list(empty_columns), [0])
        self.assertEqual(list(empty_rows), [0])
        universe = parse_universe(['#'])
        [empty_rows, empty_columns] = find_empty_rows_and_columns(universe)
        self.assertEqual(list(empty_columns), [])
        self.assertEqual(list(empty_rows), [])

    def testSimpleUniverses(self):
        universe = parse_universe([
            '..#',
            '#.#',
            '...'
        ])
        [empty_rows, empty_columns] = find_empty_rows_and_columns(universe)
        self.assertEqual(list(empty_columns), [1])
        self.assertEqual(list(empty_rows), [2])
        universe = parse_universe([
            '...',
            '...',
            '...'
        ])
        [empty_rows, empty_columns] = find_empty_rows_and_columns(universe)
        self.assertEqual(list(empty_columns), [0,1,2])
        self.assertEqual(list(empty_rows), [0,1,2])

def find_distance(c1: Coordinates, c2: Coordinates):
    return abs(c1.x - c2.x) + abs(c1.y - c2.y)

class TestFindDistance(unittest.TestCase):
    def test(self):
        self.assertEqual(find_distance(Coordinates(0,0), Coordinates(0,0)), 0)
        self.assertEqual(find_distance(Coordinates(0,0), Coordinates(0,1)), 1)
        self.assertEqual(find_distance(Coordinates(0,1), Coordinates(0,1)), 0)
        self.assertEqual(find_distance(Coordinates(0,0), Coordinates(1,1)), 2)
        self.assertEqual(find_distance(Coordinates(1,7), Coordinates(0,2)), 6)


def distance_between_all_galaxies(universe: Universe) -> int:
    return sum([find_distance(pair[0], pair[1]) for pair in combinations(universe.galaxies, 2)])

class TestFindDistanceBetweenAllGalaxies(unittest.TestCase):
    def test(self):
        lines = ['.']
        self.assertEqual(distance_between_all_galaxies(parse_universe(lines)), 0)
        lines = ['#']
        self.assertEqual(distance_between_all_galaxies(parse_universe(lines)), 0)
        lines = ['......#', '.......']
        self.assertEqual(distance_between_all_galaxies(parse_universe(lines)), 0)

    def testComplicatedUniverses(self):
        lines = [
            '.#',
            '#.'
        ]
        self.assertEqual(distance_between_all_galaxies(parse_universe(lines)), 2)
        lines = [
            '.#',
            '..',
            '#.'
        ]
        self.assertEqual(distance_between_all_galaxies(parse_universe(lines)), 3)
        lines = [
            '.#',
            '..',
            '##'
        ]
        self.assertEqual(distance_between_all_galaxies(parse_universe(lines)), 6)

    def testExampleUniverse(self):
        lines = read_input('example-input.txt')
        expanded_universe = distance_between_all_galaxies(get_expanded_universe(parse_universe(lines)))
        self.assertEqual(expanded_universe, 374)


def insert_element_at_index(arr: List, el, i: int) -> List:
    new_arr = arr[:i]
    new_arr.append(el)
    return new_arr + arr[i:]


class TestInsertElement(unittest.TestCase):
    def testInsertsElement(self):
        arr = [1,2,3]
        new_arr = insert_element_at_index(arr, 4, 0)
        self.assertEqual(arr, [1,2,3])
        self.assertEqual(new_arr, [4,1,2,3])
        new_arr = insert_element_at_index(arr, 4, 3)
        self.assertEqual(new_arr, [1,2,3,4])
        new_arr = insert_element_at_index(arr, 4, 1)
        self.assertEqual(new_arr, [1,4,2,3])
        new_arr = insert_element_at_index(arr, 4, 23)
        self.assertEqual(new_arr, [1,2,3,4])


def remove_element_at_index(arr: List, i: int) -> List:
    return arr[:i] + arr[i+1:]


class TestRemoveElement(unittest.TestCase):
    def testRemovesElement(self):
        arr = [1,2,3]
        new_arr = remove_element_at_index(arr, 0)
        self.assertEqual(new_arr, [2,3])
        self.assertEqual(arr, [1,2,3])
        new_arr = remove_element_at_index(arr, 1)
        self.assertEqual(new_arr, [1,3])
        self.assertEqual(arr, [1,2,3])
        new_arr = remove_element_at_index(arr, 2)
        self.assertEqual(new_arr, [1,2])
        self.assertEqual(arr, [1,2,3])


unittest.main()
'''
lines = read_input('input.txt')
universe = parse_universe(lines)
expanded_universe = get_expanded_universe(universe)
print('shortest path')
print(distance_between_all_galaxies(expanded_universe))
'''
