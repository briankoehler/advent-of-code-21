import math


def part_one():
    prev_measurement = math.inf
    answer = 0

    with open('input.txt', 'r') as f:
        for line in f:
            measurement = int(line)
            if measurement > prev_measurement: answer += 1
            prev_measurement = measurement

    print(f'Number of depth measurement increases: {answer}')


def part_two():
    with open('input.txt', 'r') as f:
        nums = [int(line) for line in f.readlines()]

    # Initialize values - current window is the first 2 elements
    prev_measurement = math.inf
    answer = 0
    measurement = nums[0] + nums[1]

    # Slide window of 3 elements until the end
    for i in range(2, len(nums)):
        measurement += nums[i]

        if measurement > prev_measurement: answer += 1
        prev_measurement = measurement
        
        measurement -= nums[i - 2]

    print(f'Number depth measurement increases: {answer}')
    

if __name__ == '__main__':
    part_one()
    part_two()
