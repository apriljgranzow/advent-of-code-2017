import solution as s

def test_no_dupe_words():
    examples = {
        'aa bb cc dd ee' : True,
        'aa bb cc dd aa' : False,
        'aa bb cc dd aaa' : True
    }
    for elem in examples:
        assert s.no_dupe_words(elem) == examples[elem]

