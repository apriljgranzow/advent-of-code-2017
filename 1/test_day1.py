import solution as s

def test_part_one():
    examples = {
        '1122' : 3,
        '1111' : 4,
        '1234' : 0,
        '91212129' : 9
    }
    for elem in examples:
        assert s.part_one(elem) == examples[elem]