import solution as s

def test_range_checksum():
    examples = {
        (5,1,9,5) : 8,
        (7,5,3) : 4,
        (2,4,6,8) : 6
    }
    for elem in examples:
        assert s.range_checksum(elem) == examples[elem]

def test_part_one():
    assert s.part_one([[5,1,9,5],[7,5,3],[2,4,6,8]]) == 18

def test_find_even_pair_quotient():
    examples = {
        (5,9,2,8) : 4,
        (9,4,7,3) : 3,
        (3,8,6,5) : 2
    }
    for elem in examples:
        assert s.find_even_pair_quotient(elem) == examples[elem]

def test_part_two():
    assert s.part_two([(5,9,2,8),(9,4,7,3),(3,8,6,5)]) == 9