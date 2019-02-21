import re

def parse_input(text):
    grammar = re.compile(r'(\w+) \((\d+)\) ?-?>? ?(.+)?')
    return grammar.findall(text)

def parse_match(reTuple):
    '''Take a regex match object and return a tuple of typecasted data'''
    name = reTuple[0]
    weight = int(reTuple[1])
    children = [x.strip() for x in reTuple[2].split(',')]
    return (name,weight,children)

def create_input_list(text):
    '''Take raw text, find all regex matches and then typecast'''
    return [parse_match(x) for x in parse_input(text)]

def parent_to_child_dict(inputs):
    '''Return a dictionary of parents keyed to a tuple of weight and
    list of children'''
    nodes = {}
    for elem in inputs:
        nodes[elem[0]] = (elem[1],elem[2])
    return nodes

def child_to_parent_dict(parent_dict):
    '''Return a dictionary of nodes keyed to their direct parent'''
    child_dict = {}
    for elem in parent_dict:
        if parent_dict[elem][1]: # skip leaf nodes
            for child in parent_dict[elem][1]:
                child_dict[child] = elem
    return child_dict

def weight_dict(inputs):
    data = parent_to_child_dict(inputs)
    weights = {x:data[x][0] for x in data}
    return weights

def part_one(inputs):
    '''Find the root of the tree by figuring out which node has no
    direct parent.'''
    parent_to_child = parent_to_child_dict([x for x in inputs if x[2]])
    child_to_parent = child_to_parent_dict(parent_to_child)
    return set([x[0] for x in inputs]) - set(child_to_parent.keys())

### Part Two ###
# Find a way to structure the tree so we can easily check branches
# and weights
# https://gist.github.com/hrldcpr/2012250
class Node(object):
    
    def __init__(self,name,weight,children=[]):
        '''Tree representation with arbitrary number of children stored 
        in a list'''
        self.name   = name
        self.weight = weight
        self.children = children
        self.total_weight = weight # to cache subtree weights for the final result

    def balanced_children(self):
        '''Only works on direct children, not entire subtrees'''
        return len(set([x.weight for x in self.children])) == 1

    def tree_weight(self):
        # https://www.geeksforgeeks.org/iterative-preorder-traversal-of-a-n-ary-tree/
        '''Return sum of node weights for the entire tree'''
        total = 0
        stack = []
        stack.append(self)
        total += self.weight
        while len(stack) > 0:
            current_node = stack[len(stack)-1]
            if current_node.children:
                stack.extend(current_node.children)
            else:
                total += stack.pop().weight
        self.total_weight = total
        return total

def node_children(parent,inputs):
    '''Given a node name, return a list of node objects representing its
    children'''
    children = parent_to_child_dict(inputs)[parent][1]
    if children == ['']:
        return []
    weights = weight_dict(inputs)
    return [Node(x,weights[x]) for x in children]

def build_tree(inputs):
    '''Build a tree structure given only a list of inputs'''
    name = [x for x in part_one(inputs)][0] # root name
    parent_to_children = parent_to_child_dict(inputs)
    weights = weight_dict(inputs)
    # Create nodes
    root = Node(name,weights[name],node_children(name,inputs))
    stack = []
    stack.append(root)
    while len(stack) > 0:
        current_node = stack[len(stack)-1]
        if parent_to_children[current_node.name][1]:
            current_node.children = node_children(current_node.name,inputs)
            stack.pop()
            stack.extend(current_node.children)
        else:
            stack.pop()
    return root

example = '''
                pbga (66)
                xhth (57)
                ebii (61)
                havc (66)
                ktlj (57)
                fwft (72) -> ktlj, cntj, xhth
                qoyq (66)
                padx (45) -> pbga, havc, qoyq
                tknk (41) -> ugml, padx, fwft
                jptl (61)
                ugml (68) -> gyxo, ebii, jptl
                gyxo (61)
                cntj (57)
            '''
inputs = create_input_list(example)

if __name__ == "__main__":
    with open("input.txt") as file:
        text = file.read()
    inputs = create_input_list(inputs)
    print(part_one(inputs))
    