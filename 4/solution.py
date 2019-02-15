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

def no_anagram_words(string):
    anagrams = set()
    for word in string.split():
        if ''.join(sorted(word)) in anagrams:
            return False
        else:
            anagrams.add(''.join(sorted(word)))
    return True

def part_two(stringList):
    total = 0
    for string in stringList:
        if no_anagram_words(string):
            total += 1
    return total

if __name__ == "__main__":
    with open('input.txt') as file:
        lines = file.readlines()
    print(part_one(lines))
    print(part_two(lines))