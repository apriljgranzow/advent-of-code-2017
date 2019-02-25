def part_one(charstream):
    depth = 0
    garbage = False
    ignore = False
    score = 0
    for char in charstream:
        if garbage and not ignore and char == '>':
            garbage = False
        elif garbage and not ignore and char == '!':
            ignore = True
        elif garbage and ignore:
            # ignore the current char and move on
            ignore = False
        elif not garbage and not ignore:
            if char == '{':
                depth += 1
            elif char == '<':
                garbage = True
            elif char == '!':
                ignore = True
            elif char == '}':
                score += depth
                depth -= 1
    return score

if __name__ == "__main__":
    with open("input.txt") as file:
        text = file.read()
    print(part_one(text))