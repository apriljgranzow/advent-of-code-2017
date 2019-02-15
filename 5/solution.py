from collections import defaultdict

def part_one(intList):
    array = intList[:]
    steps = 0
    i = 0
    while i < len(array):
        jump_value = (array[i])
        array[i] += 1
        i += jump_value
        steps += 1
    return steps
    
def part_two(intList):
    array = intList[:]
    steps = 0
    i = 0
    while i < len(array):
        jump_value = (array[i])
        if array[i] >= 3:
            array[i] -= 1
        else:
            array[i] += 1
        i += jump_value
        steps += 1
    return steps

if __name__ == "__main__":
    with open('input.txt') as file:
        lines = file.readlines()
    inputs = [int(x) for x in lines]
    print(part_one(inputs))
    print(part_two(inputs))