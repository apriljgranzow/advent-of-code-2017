def range_checksum(intList):
    return max(intList) - min(intList)

def part_one(inputs):
    total = 0
    for line in inputs:
        total += range_checksum(line)
    return total

if __name__ == "__main__":
    with open('input.txt') as file:
        lines = file.readlines()
    intLists = []
    for line in lines:
        intLists.append([int(x) for x in line.split()])
    print(part_one(intLists))