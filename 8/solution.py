import re
from collections import defaultdict

def get_inputs(text):
    ''' Regex split lines of text into groups.  Breakdown is as follows:
    Example: `ba dec 37 if znx != 0`
    Group 1: node to be changed if conditional is true
    Group 2: `inc` or `dec` = increase or decrease node from G1
    Group 3: amount to increase or decrease. can be pos or neg.
    Group 4: other node whose value must be known to evaluate conditional
    Group 5: conditional operator and comparison value to use with eval()
    '''
    input_format = r'(.+)\s(inc|dec)\s(-?\d+) if (.+)\s(\S+\s-?\d+)'
    grammar = re.compile(input_format)
    return grammar.findall(text)

class Instruction(object):
    def __init__(self,regex_match_object):
        self.node1 = regex_match_object[0]
        self.incdec = regex_match_object[1]
        self.inst_value = int(regex_match_object[2])
        self.node2 = regex_match_object[3]
        self.condition = regex_match_object[4]
    
def initialize_instruction_objects(inputs):
    instructions = []
    for match_object in inputs:
        instructions.append(Instruction(match_object))
    return instructions

def parse_conditional(node_val,condition_str):
    return eval(str(node_val)+condition_str)

def update_registers(instructions,register_dict=None):
    registers = defaultdict(int)
    for line in instructions:
        valid = parse_conditional(registers[line.node2],line.condition)
        if valid and line.incdec == 'inc':
            registers[line.node1] += line.inst_value
        elif valid and line.incdec == 'dec':
            registers[line.node1] -= line.inst_value
    return registers

def part_one(text):
    inputs = get_inputs(text)
    instructions = initialize_instruction_objects(inputs)
    registers = update_registers(instructions)
    return max(registers.values())

def part_two(text):
    inputs = get_inputs(text)
    instructions = initialize_instruction_objects(inputs)
    registers = defaultdict(int)
    max_seen = 0
    for line in instructions:
        valid = parse_conditional(registers[line.node2],line.condition)
        if valid and line.incdec == 'inc':
            registers[line.node1] += line.inst_value
        elif valid and line.incdec == 'dec':
            registers[line.node1] -= line.inst_value
        if registers[line.node1] > max_seen:
            max_seen = registers[line.node1]
    return max_seen

if __name__ == "__main__":
    with open("input.txt") as file:
        text = file.read()
    print(part_one(text))
    print(part_two(text))
    
