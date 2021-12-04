
def part_one():
    # Read file lines to list
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    # # Extract numbers and boards
    nums, boards = lines[0].split(sep=','), []
    for i in range(2, len(lines), 6):
        boards.append([line.split() for line in lines[i:i+5]])

    last_num, winning_board = 0, []
    called_nums = set(nums[:4])

    # Iterate called numbers
    for num in nums[4:]:
        if winning_board:
            break

        called_nums.add(num)
        last_num = num

        # Iterate boards
        for board in boards:
            if winning_board:
                break

            # Loop rows
            for row in board:
                if set(row).issubset(called_nums):
                    winning_board = board
                    break

            # Loop columns
            for i in range(len(board[0])):
                col = {test[i] for test in board}
                if col.issubset(called_nums):
                    winning_board = board
                    break

    # Get all numbers of winning board into a set
    all_nums = {inner for outer in winning_board for inner in outer}

    # Determine which are leftover and use to calculate score
    remaining = all_nums - called_nums
    s = sum(int(num) for num in remaining)

    print(f'Final score: {s * int(last_num)}')


def part_two():
    # Read file lines to list
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    # Extract numbers and boards
    nums, boards = lines[0].split(sep=','), []
    for i in range(2, len(lines), 6):
        boards.append([line.split() for line in lines[i:i+5]])

    last_num, winning_boards = 0, []
    called_nums = set()

    # Iterate called numbers
    for num in nums:
        called_nums.add(num)
        last_num = num

        # Iterate boards that remain
        for board in [board for board in boards if board not in winning_boards]:
            stop = False

            # Loop rows
            for row in board:
                if set(row).issubset(called_nums):
                    winning_boards.append(board)
                    stop = True
                    break

            if stop:
                continue

            # Loop columns
            for i in range(len(board[0])):
                col = {test[i] for test in board}
                if col.issubset(called_nums):
                    winning_boards.append(board)
                    break

        # All boards have won
        if len(winning_boards) == len(boards):
            break

    # Get all numbers of last board
    all_nums = {inner for outer in winning_boards[-1] for inner in outer}

    # Determine which are leftover and calculate score
    remaining = all_nums - called_nums
    s = sum(int(num) for num in remaining)

    print(f'Final score: {s * int(last_num)}')


if __name__ == '__main__':
    part_one()
    part_two()
