import llist as ll

def get_slice(dllist,pos,length):
    new_llist = ll.dllist()
    while length:
        if pos > len(dllist)-1:
            pos = 0
        # import pdb; pdb.set_trace()
        new_llist.append(dllist.remove(dllist.nodeat(pos)))
        length -= 1
    return new_llist

def reverse_slice(dllist,pos,length):
    ll_slice = get_slice(dllist,pos,length)
    for i in range(len(ll_slice)):
        # import pdb; pdb.set_trace()
        dllist.insert(ll_slice.popleft(),dllist.nodeat(pos))

def reverse_wrap_around(dllist,pos,length):
    '''If the slice of the linked list wraps around to the beginning,
    break it up when inserting it back into the list'''
    right_side = (pos+length) % len(dllist)
    ll_slice = get_slice(dllist,pos,length)
    while right_side:
        dllist.append(ll_slice.pop())
        right_side -= 1
    while ll_slice:
        dllist.appendleft(ll_slice.pop())

def part_one(lengths,number=256):
    # begin with a list of numbers from 0 to 255
    numbers = ll.dllist(range(number))
    print(f"Initial list = {numbers}")
    # current position starts at 0
    pos = 0
    skip = 0
    for length in lengths:
        # *Reverse* the order of that *length* of elements in the *list*, 
        # starting with the element at the *current position*.
        if pos+length > number:
            pass
        reverse_slice(numbers,pos,length)
        # *Move* the *current position* forward by that *length* plus the 
        # *skip size*.
        pos = (pos+length+skip) % number
        # *Increase* the *skip size* by one.
        skip += 1
        print(numbers)
    return numbers

if __name__ == "__main__":
    with open("input.txt") as file:
        text = file.read()
    inputs = [int(x) for x in text.split(',')]
    print(part_one([3,4,1,5],number=5))
    # print(part_one(inputs))