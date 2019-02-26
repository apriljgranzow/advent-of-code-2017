import solution as s

def test_part_one():
    examples = {
        r'{}'       : 1,
        r'{{{}}}'   : 6,
        r'{{},{}}'  : 5,
        r'{{{},{},{{}}}}'       : 16,
        r'{<a>,<a>,<a>,<a>}'    : 1,
        r'{{<ab>},{<ab>},{<ab>},{<ab>}}'    : 9,
        r'{{<!!>},{<!!>},{<!!>},{<!!>}}'    : 9,
        r'{{<a!>},{<a!>},{<a!>},{<ab>}}'    : 3
    }
    for elem in examples:
        assert s.part_one(elem) == examples[elem]

def test_part_two():
    examples = {
	'<>' :  0,
	'<random characters>' :  17,
	'<<<<>' :  3,
	'<{!>}>' :  2,
	'<!!>' :  0,
	'<!!!>>' :  0,
	'<{o"i!a,<{i<a>' :  10
    }
    for elem in examples:
        assert s.part_two(elem) == examples[elem]