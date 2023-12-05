import unittest
from functools import reduce
import copy

def read_input(filename = 'input.txt'):
    with open(filename, 'r') as f:
        return f.readlines()

'''
Card
index: number # 1-indexed
winning_numbers: Set<number>
your_numbers: Set<number>
'''

def parse_card(line):
    [card_string, numbers_string] = line.split(':')
    card_number = int(card_string[len('Card '):])
    [winning_numbers_string, your_numbers_string] = numbers_string.split(' | ')
    winning_numbers = [int(n) for n in [item for item in winning_numbers_string.split(' ') if item != '']]
    your_numbers = [int(n) for n in [item for item in your_numbers_string.split(' ') if item != '']]

    return {
        'index': card_number,
        'winning_numbers': set(winning_numbers),
        'your_numbers': set(your_numbers)
    }

class TestParseCard(unittest.TestCase):
    def test_card_index(self):
        line = 'Card 1: 123 | 123'
        card = parse_card(line)
        self.assertEqual(card['index'], 1)
        line = 'Card 12: 1 23 2 3 4 | 12 9 3 0'
        card = parse_card(line)
        self.assertEqual(card['index'], 12)

    def test_number_sets(self):
        line = 'Card 1: 123 | 123'
        card = parse_card(line)
        self.assertCountEqual(card['winning_numbers'], set([123]))
        self.assertCountEqual(card['your_numbers'], set([123]))

        line = 'Card 12: 1 23 2 3 4 | 12 9 3 0'
        card = parse_card(line)
        self.assertCountEqual(card['winning_numbers'], set([1,23,2,3,4]))
        self.assertCountEqual(card['your_numbers'], set([12,9,3,0]))

def get_card_score(card):
    count_matching_elements = len(card['winning_numbers'].intersection(card['your_numbers']))
    if count_matching_elements == 0:
        return 0
    else:
        return 2 ** (count_matching_elements - 1)


class TestCardScore(unittest.TestCase):
    def test_no_match(self):
        card = parse_card('Card 1: 1 2 3 | 4 5 6')
        self.assertEqual(get_card_score(card), 0)

    def test_1_match(self):
        card = parse_card('Card 123: 1 2 33 | 33 0 12')
        self.assertEqual(get_card_score(card), 1)

    def test_order_does_not_matter(self):
        card = parse_card('Card 100: 1 2 3 | 1 4 3')
        self.assertEqual(get_card_score(card), 2)
        card = parse_card('Card 110: 1 2 3 | 3 4 1')
        self.assertEqual(get_card_score(card), 2)


def read_and_score_card_input(filename = 'input.txt'):
    lines = read_input(filename)
    
    def add(a, b):
        return a + b

    return reduce(add, [get_card_score(card) for card in [parse_card(line) for line in lines]])

# print(read_and_score_card_input('input.txt'))

def count_matching_numbers(card):
    return len(card['winning_numbers'].intersection(card['your_numbers']))

def read_and_count_cards(cards):
    reference_cards = cards
    my_cards = [dict(d) for d in reference_cards]

    card_index = 0

    while card_index < len(my_cards):
        card = my_cards[card_index]
        matching_numbers_count = count_matching_numbers(card)
        for i in range(matching_numbers_count):
            index_to_add = i + card['index']
            new_card = reference_cards[index_to_add]
            my_cards.append(new_card)
        card_index += 1

    return len(my_cards)

class TestReadAndCountCards(unittest.TestCase):
    def test_no_match(self):
        lines = [
            'Card 1: 1 2 3 | 4 5 6'
        ]
        cards = [parse_card(line) for line in lines]
        self.assertEqual(read_and_count_cards(cards), 1)

        lines = [
            'Card 1: 1 2 3 | 4 5 6',
            'Card 12: 4 5 6 | 7 8 9'
        ]
        cards = [parse_card(line) for line in lines]
        self.assertEqual(read_and_count_cards(cards), 2)

    def test_1_match(self):
        lines = [
            'Card 1: 1 2 3 | 1 4 5',
            'Card 2: 1 2 3 | 4 5 6'
        ]
        cards = [parse_card(line) for line in lines]
        self.assertEqual(read_and_count_cards(cards), 3)

    def test_example(self):
        lines = read_input('example-input.txt')
        cards = [parse_card(line) for line in lines]
        self.assertEqual(read_and_count_cards(cards), 30)

#unittest.main()

lines = read_input('input.txt')
cards = [parse_card(line) for line in lines]
print(read_and_count_cards(cards))
