import solution as s

def test_redistribute():
    examples = [
        [0,2,7,0],
        [2,4,1,2],
        [3,1,2,3],
        [0,2,3,4],
        [1,3,4,1],
        [2,4,1,2]
    ]
    for i in range(0,len(examples)-1):
        assert s.redistribute(examples[i]) == examples[i+1]

def test_part_one():
    assert s.part_one([0,2,7,0]) == 5

def test_part_two():
    assert s.part_two([0,2,7,0]) == 4