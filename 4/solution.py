def no_dupe_words(string):
    words = set()
    for word in string.split():
        if word in words:
            return False
        else:
            words.add(word)
    return True

def part_one(stringList):
    total = 0
    for string in stringList:
        if no_dupe_words(string):
            total += 1
    return total

if __name__ == "__main__":
    with open('input.txt') as file:
        lines = file.readlines()
    print(part_one(lines))