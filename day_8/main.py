
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

    code = {}

    for line in lines:
        tokens = line.split(sep='|')
        signals, output = tokens[0], tokens[1]

        for s in signals:
            if len(s) == 2: code[s] = 1
            elif len(s) == 3: code[s] = 7
            elif len(s) == 4: code[s] = 4
            elif len(s) == 7: code[s] = 8
            else:
                ...
            

if __name__ == '__main__':
    part_one()
    part_two()
