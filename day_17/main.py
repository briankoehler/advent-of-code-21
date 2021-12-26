
def part_one():
    with open('input.txt') as f:
        line = f.readline().strip()

    # Process textual data
    x_index, comma = line.index('x='), line.index(',')
    x_data = line[x_index+2:comma].split(sep='..')
    y_data = line[comma+4:].split(sep='..')
    x_data, y_data = tuple(int(x) for x in x_data), tuple(int(y) for y in y_data)


    

def part_two():
    ...


if __name__ == '__main__':
    part_one()
    part_two()
