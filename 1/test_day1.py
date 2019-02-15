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

def test_groupby_indices_halfway_round():
    examples = {
        '1212' : [('1','1'),('2','2')],
        '1221' : [('1','2'),('2','1')],
        '123425' : [('1','4'), ('2','2'),('3','5')],
        '123123' : [('1','1'), ('2','2'),('3','3')],
        '12131415' : [('1','1'), ('2','4'),('1','1'),('3','5')]
    }
    for elem in examples:
        assert s.groupby_indices_halfway_round(elem) == examples[elem]

def test_part_two():
    examples = {
        '1212' : 6,
        '1221' : 0,
        '123425' : 4,
        '123123' : 12,
        '12131415' : 4
    }
    for elem in examples:
        assert s.part_two(elem) == examples[elem]