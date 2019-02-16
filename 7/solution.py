import re
# (\w+) (\(\d+\)) ?-?>? ?(.+)?

def parse_input(text):
    grammar = re.compile(r'(\w+) \((\d+)\) ?-?>? ?(.+)?')
    return grammar.findall(text)

def parse_match(reTuple):
    '''Take a regex match object and return a tuple of typecasted data'''
    name = reTuple[0]
    weight = int(reTuple[1])
    children = [x.strip() for x in reTuple[2].split(',')]
    return (name,weight,children)

def dict_matches(inputs):
    '''Return a dictionary of parents keyed to a tuple of weight and
    list of children'''
    nodes = {}
    for elem in inputs:
        nodes[elem[0]] = (elem[1],elem[2])
    return nodes

def children_dict(parent_dict):
    child_dict = {}
    for elem in parent_dict:
        for child in parent_dict[elem][1]:
            child_dict[child] = elem
    return child_dict

def part_one(inputs):
    parent_to_child = dict_matches([x for x in inputs if x[2]])
    child_to_parent = children_dict(parent_to_child)
    return set([x[0] for x in inputs]) - set(child_to_parent.keys())

if __name__ == "__main__":
    with open("input.txt") as file:
        text = file.read()
    inputs = [parse_match(x) for x in parse_input(text)]
    print(part_one(inputs))