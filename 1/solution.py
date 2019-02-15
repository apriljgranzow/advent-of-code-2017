def part_one(intStr):
    total = 0
    for i in range(len(intStr)):
        j = (i + 1) % len(intStr)
        if intStr[i] == intStr[j]:
            total += int(intStr[i])
    return total

if __name__ == "__main__":
    with open('input.txt') as file:
        inputStr = file.read()
    print(part_one(inputStr))