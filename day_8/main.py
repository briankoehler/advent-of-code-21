
def part_one():
    with open('input.txt') as f:
        lines = f.readlines()

    answer = 0

    for line in lines:
        output = line.split(sep='|')[1]
        tokens = output.split()

        for t in tokens:
            if len(t) in (2, 3, 4, 7): answer += 1

    print(f'1, 4, 7, or 8 appear {answer} times')


def part_two():
    with open('input.txt') as f:
        lines = f.readlines()

    code, answer = {}, 0

    for line in lines:
        tokens = line.split(sep='|')
        signals, output = tokens[0].split(), tokens[1].split()
        visited = set()

        # On first loop through the signals, get base cases of 1, 7, 4, 8 (unique lengths)
        for s in signals:
            s = frozenset(s)
            if s in visited: continue

            if len(s) == 2:
                code[s], code[1] = '1', s
                visited.add(s)
            elif len(s) == 3:
                code[s], code[7] = '7', s
                visited.add(s)
            elif len(s) == 4:
                code[s], code[4] = '4', s
                visited.add(s)
            elif len(s) == 7:
                code[s], code[8] = '8', s
                visited.add(s)

        # On second loop, decode 3, 6, 9, 0 using supersets and lengths
        for s in signals:
            s = frozenset(s)
            if s in visited: continue

            if len(s) == 5 and s.issuperset(code[1]):
                code[s], code[3] = '3', s
                visited.add(s)
            elif len(s) == 6 and not s.issuperset(code[7]):
                code[s], code[6] = '6', s
                visited.add(s)
            elif len(s) == 6 and s.issuperset(code[4]):
                code[s], code[9] = '9', s
                visited.add(s)
            elif len(s) == 6:
                code[s], code[0] = '0', s
                visited.add(s)

        # On last loop, decode 2, 5 because 5 relies on having 6 decoded, and 2 is whatever is left
        for s in signals:
            s = frozenset(s)
            if s in visited: continue

            if len(s) == 5 and s.issubset(code[6]):
                code[s], code[5] = '5', s
            elif len(s) == 5:
                code[s], code[2] = '2', s

        num = ''
        for token in output:
            num += code[frozenset((token))]
        answer += int(num)

    print(f'Sum of values is {answer}')


if __name__ == '__main__':
    part_one()
    part_two()
