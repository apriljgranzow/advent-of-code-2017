def range_checksum(intList):
    return max(intList) - min(intList)

def part_one(inputs):
    total = 0
    for line in inputs:
        total += range_checksum(line)
    return total

def find_even_pair_quotient(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and (lst[i] % lst[j] == 0):
                return lst[i] / lst[j]
            elif i != j and (lst[j] % lst[i] == 0):
                return lst[j] / lst[i]

def part_two(inputs):
    total = 0
    for line in inputs:
        total += find_even_pair_quotient(line)
    return total

if __name__ == "__main__":
    with open('input.txt') as file:
        lines = file.readlines()
    intLists = []
    for line in lines:
        intLists.append([int(x) for x in line.split()])
    print(part_one(intLists))
    print(part_two(intLists))