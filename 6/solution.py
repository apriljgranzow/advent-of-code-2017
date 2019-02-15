from operator import itemgetter

def redistribute(intList):
    new_list = intList[:]
    indices_and_values = enumerate(intList)
    max_index, max_value = max(indices_and_values,key=itemgetter(1))
    d,r = divmod(max_value,len(intList)-1)
    if d == 0:
        for i in range(max_index+1,max_index+max_value+1):
            new_list[i%len(new_list)] += 1
        new_list[max_index] = 0
    else:
        for i in range(len(new_list)):
            if i != max_index:
                new_list[i] += d
            else:
                new_list[i] = r
    return new_list

def part_one(intList):
    new_list = intList[:]
    configurations = set() # can't hash lists so we will cast to string
    loops = 0
    while True:
        loops += 1
        new_list = redistribute(new_list)
        if str(new_list) in configurations:
            return loops
        else:
            configurations.add(str(new_list))

def part_two(intList):
    new_list = intList[:]
    configurations = set() # can't hash lists so we will cast to string
    loops = 0
    repeated_configuration = None
    while True:
        loops += 1
        new_list = redistribute(new_list)
        if str(new_list) == repeated_configuration:
            return loops
        elif str(new_list) in configurations:
            repeated_configuration = str(new_list)
            loops = 0
            configurations = set()
        else:
            configurations.add(str(new_list))

if __name__ == "__main__":
    with open("input.txt") as file:
        text = file.read()
    array = [int(x) for x in text.split()]
    print(part_one(array))
    print(part_two(array))