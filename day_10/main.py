
def part_one():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    openers = {')': '(', ']': '[', '}': '{', '>': '<'}
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0

    for line in lines:
        stack = []

        for c in line:
            if c in ('(', '{', '[', '<'): stack.append(c)
            elif stack.pop() != openers[c]: score += points[c]

    print(f'Total syntax error score: {score}')


def part_two():
    with open('input.txt') as f:
        lines = f.read().splitlines()

    openers = {')': '(', ']': '[', '}': '{', '>': '<'}
    points = {'(': 1, '[': 2, '{': 3, '<': 4}
    scores = []

    for line in lines:
        stack, error, score = [], False, 0

        for c in line:
            if c in ('(', '{', '[', '<'): stack.append(c)
            elif stack.pop() != openers[c]: error = True

        if error: continue
        while stack: score = score * 5 + points[stack.pop()]
        scores.append(score)

    winner = sorted(scores)[len(scores) // 2]
    print(f'Middle score: {winner}')


if __name__ == '__main__':
    part_one()
    part_two()
