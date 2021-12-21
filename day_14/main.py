from collections import defaultdict


def part_one():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    template, raw_rules = lines[0], lines[2:]
    rules = {}

    # Construct rules mapping
    for r in raw_rules:
        key, value = r.split(sep=' -> ')
        rules[key] = value
    
    # Construct new string
    for _ in range(10):
        i = 0
        while i <= len(template) - 1:
            pair = template[i:i+2]
            if pair in rules:
                template = template[:i+1] + rules[pair] + template[i+1:]
                i += 2
            else:
                i += 1

    # Count characters
    counts = defaultdict(int)
    for c in template:
        counts[c] += 1
    
    min_count, max_count = min(counts.values()), max(counts.values())

    print(f'Difference: {max_count - min_count}')


def part_two():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    template, raw_rules = lines[0], lines[2:]
    rules = {}

    # Construct rules mapping
    for r in raw_rules:
        key, value = r.split(sep=' -> ')
        rules[key] = value

    # Count current pairs
    pairs = defaultdict(int)
    for x in range(len(template) - 1):
        pairs[template[x:x+2]] += 1

    # Count current characters
    counts = defaultdict(int)
    for c in template:
        counts[c] += 1
    
    # Rather than constructing the string everytime, determine change in counts and pairs
    # Reduce pair count by original amount, but add new pairs too
    # Increase character count by number of pairs that add that character
    # e.g. 'AB' -> 'ACB' causes pairs['AB'] -= 1, pairs['AC'] += 1, pairs['CB'] += 1
    # cont'd: Take number of 'AB' and change pairs values by same amount (instead of 1) to determine changes
    for _ in range(40):
        new_pairs = pairs.copy()
        for p in pairs:
            new_pairs[p] -= pairs[p]
            new_pairs[p[0] + rules[p]] += pairs[p]
            new_pairs[rules[p] + p[1]] += pairs[p]
            counts[rules[p]] += pairs[p]
        pairs = new_pairs

    print(f'Difference: {max(counts.values()) - min(counts.values())}')


if __name__ == '__main__':
    part_one()
    part_two()
