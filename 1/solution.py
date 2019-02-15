def part_one(intStr):
    total = 0
    for i in range(len(intStr)):
        j = (i + 1) % len(intStr)
        if intStr[i] == intStr[j]:
            total += int(intStr[i])
    return total

def groupby_indices_halfway_round(iterable):
    median = len(iterable)//2
    return list(zip(iterable[:median],iterable[median:]))

def part_two(intStr):
    tuple_list = groupby_indices_halfway_round(intStr)
    total = 0
    for pair in tuple_list:
        if pair[0] == pair[1]:
            total += int(pair[0])*2
    return total

if __name__ == "__main__":
    with open('input.txt') as file:
        inputStr = file.read()
    print(part_one(inputStr))
    print(part_two(inputStr))