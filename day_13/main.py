
def part_one():
    with open('input.txt') as f:
        lines = f.read()

    # Breakdown dots to set of tuples and folds into list of strings
    dots, folds = lines.split('\n\n')
    dots, folds = dots.splitlines(), folds.splitlines()
    dots = set(tuple(int(n) for n in dot.split(sep=',')) for dot in dots)

    # Return removals and additions to dots set after flip
    def flip_dots(axis, value):
        removals, additions = set(), set()

        for dot in dots:
            if dot[axis] > value:
                removals.add(dot)
                flipped_value = value - (dot[axis] - value)
                if flipped_value >= 0:
                    new_dot = (dot[0], flipped_value) if axis == 1 else (flipped_value, dot[1])
                    additions.add(new_dot)

        return removals, additions

    # Determine what kind of flip to do
    if 'y=' in folds[0]: axis, fold = 1, int(folds[0].split(sep='=')[1])
    if 'x=' in folds[0]: axis, fold = 0, int(folds[0].split(sep='=')[1])
            
    # Flip necessary dots and mutate set of dots
    removals, additions = flip_dots(axis, fold)
    dots = dots - removals | additions

    print(f'Number of visible dots: {len(dots)}')


def part_two():
    with open('input.txt') as f:
        lines = f.read()

    # Breakdown dots to set of tuples and folds into list of strings
    dots, folds = lines.split('\n\n')
    dots, folds = dots.splitlines(), folds.splitlines()
    dots = set(tuple(int(n) for n in dot.split(sep=',')) for dot in dots)

    # Return removals and additions to dots set after flip
    def flip_dots(axis, value):
        removals, additions = set(), set()

        for dot in dots:
            if dot[axis] > value:
                removals.add(dot)
                flipped_value = value - (dot[axis] - value)
                if flipped_value >= 0:
                    new_dot = (dot[0], flipped_value) if axis == 1 else (flipped_value, dot[1])
                    additions.add(new_dot)

        return removals, additions

    # Determine what kind of flip to do
    for f in folds:
        if 'y=' in f: axis, fold = 1, int(f.split(sep='=')[1])
        if 'x=' in f: axis, fold = 0, int(f.split(sep='=')[1])
            
        # Flip necessary dots and mutate set of dots
        removals, additions = flip_dots(axis, fold)
        dots = dots - removals | additions

    max_x = max(dots, key=lambda dot: dot[0])[0]
    max_y = max(dots, key=lambda dot: dot[1])[1]

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) in dots: print('#', end='')
            else: print('.', end='')
        print()


if __name__ == '__main__':
    part_one()
    part_two()
