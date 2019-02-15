from collections import defaultdict

def part_one(intList):
    steps = 0
    i = 0
    while i < len(intList):
        jump_value = (intList[i])
        intList[i] += 1
        i += jump_value
        steps += 1
    return steps

if __name__ == "__main__":
    with open('input.txt') as file:
        lines = file.readlines()
    inputs = [int(x) for x in lines]
    print(part_one(inputs))