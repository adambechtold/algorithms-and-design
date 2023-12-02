from functools import reduce

def read_input(filename = 'input.txt'):
    lines = []
    with open(filename, 'r') as f:
        while True:
            line = f.readline().strip()
            if line:
                lines.append(line)
            else:
                return lines

#print(read_input())

lines = read_input()
one_game_string = lines[0]
#print(one_game_string) # Game 1: 9 red, 5 blue, 6 green; 6 red, 13 blue; 2 blue, 7 green, 5 red

MAX_COUNTS = {
    'red': 12,
    'green': 13,
    'blue': 14
}

'''
type Game
index: number // 1-indexed
counts: Count[]

type Count
color: 'red' | 'blue' | 'green'
number: number
'''


def parse_game(s): 
    # Get "Game #:"
    game_string = s.split(':')[0]
    sets_string = s.split(':')[1]

    game_prefix = "Game "
    game_number = int(game_string[len(game_prefix):])

    # Get counts for all sets
    # [
    #   [[9, 'red'], [5, 'blue'], [6, 'green']]
    # ]
    sets_strings = sets_string.split(';')
    counts = []
    for sets_string in sets_strings:
        set_counts = parse_set(sets_string)
        counts.append(set_counts)


    return {
        'index': game_number,
        'counts': counts
    }

def parse_set(s):
# Example - 9 red, 5 blue, 6 green
# Reutrn = [[9, 'red'], [5, 'blue'], [6, 'green']]
    count_strings = s.split(',')
    counts = []
    for count_string in count_strings:
        #print('        get count for: ', count_string)
        [number, color] = count_string.strip().split(' ')
        counts.append([int(number), color])

    return counts


one_game = parse_game(one_game_string)
#print(one_game)


def is_game_possible(game, max_counts):
    for round_counts in game['counts']:
        for [number, color] in round_counts:
            if number > max_counts[color]:
                return False
    return True

#print(is_game_possible(one_game, MAX_COUNTS))

print('======== PART 1 ========')

possible_game_indices = []
for game in [parse_game(line) for line in lines]:
    #print('game', game)
    if is_game_possible(game, MAX_COUNTS):
        possible_game_indices.append(game['index'])
        #print('    ...is possible ✅')
    else:
        continue
        #print('    ...is not possible ❌ ')

print(sum(possible_game_indices))

def power_of_game(game):
    max_counts = {
        'red': 0,
        'blue': 0,
        'green': 0
    }

    for round in game['counts']:
        for [number, color] in round:
            if max_counts[color] < number:
                max_counts[color] = number

    def multiply(a, b):
        return a * b

    #print(max_counts)

    power = reduce(multiply, [value for item, value in max_counts.items()])
    return power

#print('game:', one_game_string)
#print('    power:', power_of_game(one_game))

print('======== PART 2 ========')

print(sum([power_of_game(game) for game in [parse_game(line) for line in lines]]))




